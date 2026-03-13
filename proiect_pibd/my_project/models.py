from django.db import models


# --- AUTH AND SYSTEM TABLES (keep mostly managed = False) --- #

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

    def __str__(self):
        return self.name


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', on_delete=models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

    def __str__(self):
        return self.codename


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, on_delete=models.DO_NOTHING, related_name='permissions')
    permission = models.ForeignKey(AuthPermission, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

    def __str__(self):
        return self.username


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete=models.DO_NOTHING, related_name='groups')
    group = models.ForeignKey(AuthGroup, on_delete=models.DO_NOTHING, related_name='users')

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, on_delete=models.DO_NOTHING, related_name='user_permissions')
    permission = models.ForeignKey(AuthPermission, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

    def __str__(self):
        return f"{self.app_label}.{self.model}"


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey(DjangoContentType, on_delete=models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, on_delete=models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'



class Shops(models.Model):
    id = models.AutoField(primary_key=True, db_column = 'idshops')
    name = models.CharField(max_length=45, db_column = 'denumire')
    address = models.CharField(max_length=45, unique=True, db_column = 'adresa')
    nr_produse = models.IntegerField(blank=True, null=True, db_column = 'nr_produse')

    class Meta:
        db_table = 'shops'

    def __str__(self):
        return self.name


class Persons(models.Model):
    id = models.AutoField(primary_key=True, db_column = 'idpersons')
    first_name = models.CharField(max_length=45, db_column='prenume')
    last_name = models.CharField(max_length=45, db_column='nume')
    email = models.CharField(max_length=45,db_column='email')

    class Meta:
        db_table = 'persons'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Memberships(models.Model):
    id = models.AutoField(primary_key=True, db_column='idmemberships')
    type = models.CharField(max_length=45, blank=True, null=True, db_column = 'tip')
    shop = models.ForeignKey(
        Shops,
        on_delete=models.PROTECT,
        related_name='memberships',
        db_column='idshops'
    )
    person = models.ForeignKey(
        Persons,
        on_delete=models.PROTECT,
        related_name='memberships',
        db_column='idpersons'
    )

    class Meta:
        db_table = 'memberships'
        unique_together = ('shop', 'person')

    def __str__(self):
        return f"{self.person} -> {self.shop} ({self.type})"
