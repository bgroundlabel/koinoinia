# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuditLog(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    record_pk = models.CharField(db_column='RECORD_PK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT')  # Field name made lowercase.
    data_old = models.JSONField(db_column='DATA_OLD', blank=True, null=True)  # Field name made lowercase.
    data_new = models.JSONField(db_column='DATA_NEW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'audit_log'
        db_table_comment = 'Audit générique pour tables T_ et F_'


class AuditLogPar(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    record_pk = models.CharField(db_column='RECORD_PK', max_length=255, blank=True, null=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    change_at = models.DateTimeField(db_column='CHANGE_AT')  # Field name made lowercase.
    data_old = models.JSONField(db_column='DATA_OLD', blank=True, null=True)  # Field name made lowercase.
    data_new = models.JSONField(db_column='DATA_NEW', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'audit_log_par'
        db_table_comment = 'Audit générique pour tables PAR_'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
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


class FFgnRakitra(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment="Identifiant unique an'ny rakitra tsirairay adika soratra")  # Field name made lowercase.
    date = models.DateField(db_column='DATE', db_comment='Date/Andro nanaovana ny rakitra')  # Field name made lowercase.
    fidirana_laharana = models.CharField(db_column='FIDIRANA_LAHARANA', max_length=100, db_comment='Fidirana voalohany, fidirana faharoa, sns.')  # Field name made lowercase.
    karazana_rakitra = models.ForeignKey('ParFKarazanaRakitra', models.DO_NOTHING, db_column='KARAZANA_RAKITRA_ID', blank=True, null=True, db_comment="Karazan'ny rakitra natao")  # Field name made lowercase.
    montant = models.DecimalField(db_column='MONTANT', max_digits=20, decimal_places=2, blank=True, null=True, db_comment="Lelavola fitambaran'ny rakitra natao")  # Field name made lowercase.
    mpanome_vola_id = models.BigIntegerField(db_column='MPANOME_VOLA_ID', blank=True, null=True, db_comment="Identifiant an'ny mpiangona nanome vola (matetika raki-pisaorana)")  # Field name made lowercase.
    mpanome_vola_libelle = models.CharField(db_column='MPANOME_VOLA_LIBELLE', max_length=100, db_comment="Anaran'ny mpanome ny vola rakitra (indrindra raha tsy mpiangona fa fikambanana na sampana)")  # Field name made lowercase.
    nomena_vola_id = models.BigIntegerField(db_column='NOMENA_VOLA_ID', blank=True, null=True, db_comment="Identifiant an'ny mpiangona nomena ny vola (ohatra : ny mpitandrina, olona hafa, sns.)")  # Field name made lowercase.
    nomena_vola_libelle = models.CharField(db_column='NOMENA_VOLA_LIBELLE', max_length=100, db_comment="Anaran'ny nomena ny vola : indrindra raha tsy mpiangona fa fikambanana na sampana, na olona ivelan'ny fiangonana mihitsy.")  # Field name made lowercase.
    validation_code = models.ForeignKey('ParFValidationCodes', models.DO_NOTHING, db_column='VALIDATION_CODE', db_comment='Code de validation, arakaraka ny dingana validation vita')  # Field name made lowercase.
    validateur1_code = models.ForeignKey('ParFValidateursVola', models.DO_NOTHING, db_column='VALIDATEUR1_CODE', blank=True, null=True, db_comment="Code an'ny validateur voalohany (mampiseho ny anarany fohy)")  # Field name made lowercase.
    validateur1_nom = models.CharField(db_column='VALIDATEUR1_NOM', max_length=200, blank=True, null=True, db_comment="Anarana lava, an'iny validateur voalohany")  # Field name made lowercase.
    validateur1_andraikitra = models.CharField(db_column='VALIDATEUR1_ANDRAIKITRA', max_length=255, blank=True, null=True, db_comment='Andraikitry ny validateur voalohany')  # Field name made lowercase.
    validateur2_code = models.ForeignKey('ParFValidateursVola', models.DO_NOTHING, db_column='VALIDATEUR2_CODE', related_name='ffgnrakitra_validateur2_code_set', blank=True, null=True, db_comment="Anarana fohy, an'ny validateur faharoa")  # Field name made lowercase.
    validateur2_nom = models.CharField(db_column='VALIDATEUR2_NOM', max_length=200, blank=True, null=True, db_comment="Anarana lava, an'ny validateur faharoa")  # Field name made lowercase.
    validateur2_andraikitra = models.CharField(db_column='VALIDATEUR2_ANDRAIKITRA', max_length=255, blank=True, null=True, db_comment='Andraikitry ny validateur faharoa')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'f_fgn_rakitra'
        unique_together = (('date', 'fidirana_laharana', 'karazana_rakitra'),)
        db_table_comment = 'Firaketana ny rakitra samihafa natao tao am-piangonana'


class FFgnVokatra(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment='Identifiant unique')  # Field name made lowercase.
    date = models.DateField(db_column='DATE', db_comment='Date / andro nanatanterahana ny vokatra')  # Field name made lowercase.
    mpiangona = models.ForeignKey('TMpiangona', models.DO_NOTHING, db_column='MPIANGONA_ID', blank=True, null=True, db_comment="Identifiant an'ny mpiangona nanao ny vokatra")  # Field name made lowercase.
    motif = models.CharField(db_column='MOTIF', max_length=100, db_comment="Anton'ny vokatra / motif an'ilay fanomezana")  # Field name made lowercase.
    montant = models.DecimalField(db_column='MONTANT', max_digits=20, decimal_places=2)  # Field name made lowercase.
    omena_ny_fgn = models.SmallIntegerField(db_column='OMENA_NY_FGN', db_comment='VRAI = Omena/atolotra ny fiangonana ilay vokatra (voka-dehibe) ; FAUX = atolotra ny Sampana na fikambanana na vondrona hafa ilay vola vokatra.')  # Field name made lowercase.
    beneficiaire_nom = models.CharField(db_column='BENEFICIAIRE_NOM', max_length=200, blank=True, null=True, db_comment="Anarana feno an'izay tolorana ny vokatra (ankoatra ny Fiangonana)")  # Field name made lowercase.
    validation_code = models.ForeignKey('ParFValidationCodes', models.DO_NOTHING, db_column='VALIDATION_CODE', db_comment='Code de validation, arakaraka ny dingana validation vita')  # Field name made lowercase.
    validateur1_code = models.ForeignKey('ParFValidateursVola', models.DO_NOTHING, db_column='VALIDATEUR1_CODE', blank=True, null=True, db_comment="Code an'ny validateur voalohany (mampiseho ny anarany fohy)")  # Field name made lowercase.
    validateur1_nom = models.CharField(db_column='VALIDATEUR1_NOM', max_length=200, blank=True, null=True, db_comment="Anarana lava, an'iny validateur voalohany")  # Field name made lowercase.
    validateur1_andraikitra = models.CharField(db_column='VALIDATEUR1_ANDRAIKITRA', max_length=255, blank=True, null=True, db_comment='Andraikitry ny validateur voalohany')  # Field name made lowercase.
    validateur2_code = models.ForeignKey('ParFValidateursVola', models.DO_NOTHING, db_column='VALIDATEUR2_CODE', related_name='ffgnvokatra_validateur2_code_set', blank=True, null=True, db_comment="Code an'ny validateur faharoa (mampiseho ny anarany fohy)")  # Field name made lowercase.
    validateur2_nom = models.CharField(db_column='VALIDATEUR2_NOM', max_length=200, blank=True, null=True, db_comment="Anarana lava, an'iny validateur faharoa")  # Field name made lowercase.
    validateur2_andraikitra = models.CharField(db_column='VALIDATEUR2_ANDRAIKITRA', max_length=255, blank=True, null=True, db_comment='Andraikitry ny validateur faharoa')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'f_fgn_vokatra'
        unique_together = (('date', 'mpiangona', 'motif'),)
        db_table_comment = 'Lisitry ny vokatra rehefa voaray'


class FMpandrayAdidyMensuel(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE')  # Field name made lowercase.
    mpandray = models.ForeignKey('TMpiangona', models.DO_NOTHING, db_column='MPANDRAY_ID')  # Field name made lowercase.
    mois_code = models.ForeignKey('ParFPeriodesMois', models.DO_NOTHING, db_column='MOIS_CODE')  # Field name made lowercase.
    montant = models.DecimalField(db_column='MONTANT', max_digits=20, decimal_places=2)  # Field name made lowercase.
    validation_code = models.ForeignKey('ParFValidationCodes', models.DO_NOTHING, db_column='VALIDATION_CODE')  # Field name made lowercase.
    validateur1_code = models.ForeignKey('ParFValidateursVola', models.DO_NOTHING, db_column='VALIDATEUR1_CODE', blank=True, null=True)  # Field name made lowercase.
    validateur1_nom = models.CharField(db_column='VALIDATEUR1_NOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    validateur1_andraikitra = models.CharField(db_column='VALIDATEUR1_ANDRAIKITRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    validateur2_code = models.ForeignKey('ParFValidateursVola', models.DO_NOTHING, db_column='VALIDATEUR2_CODE', related_name='fmpandrayadidymensuel_validateur2_code_set', blank=True, null=True)  # Field name made lowercase.
    validateur2_nom = models.CharField(db_column='VALIDATEUR2_NOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    validateur2_andraikitra = models.CharField(db_column='VALIDATEUR2_ANDRAIKITRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'f_mpandray_adidy_mensuel'
        unique_together = (('date', 'mpandray', 'mois_code'),)
        db_table_comment = "Lisitry ny fandoavana Adidy isam-bolana an'ny Mpandray ny F"


class FMpiangonaAdidyAnnuel(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    date = models.DateField(db_column='DATE')  # Field name made lowercase.
    mpiangona = models.ForeignKey('TMpiangona', models.DO_NOTHING, db_column='MPIANGONA_ID')  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=100)  # Field name made lowercase.
    montant = models.DecimalField(db_column='MONTANT', max_digits=20, decimal_places=2)  # Field name made lowercase.
    validation_code = models.ForeignKey('ParFValidationCodes', models.DO_NOTHING, db_column='VALIDATION_CODE')  # Field name made lowercase.
    validateur1_code = models.ForeignKey('ParFValidateursVola', models.DO_NOTHING, db_column='VALIDATEUR1_CODE', blank=True, null=True)  # Field name made lowercase.
    validateur1_nom = models.CharField(db_column='VALIDATEUR1_NOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    validaetur1_andraikitra = models.CharField(db_column='VALIDAETUR1_ANDRAIKITRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    validateur2_code = models.ForeignKey('ParFValidateursVola', models.DO_NOTHING, db_column='VALIDATEUR2_CODE', related_name='fmpiangonaadidyannuel_validateur2_code_set', blank=True, null=True)  # Field name made lowercase.
    validateur2_nom = models.CharField(db_column='VALIDATEUR2_NOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    validateur2_andraikitra = models.CharField(db_column='VALIDATEUR2_ANDRAIKITRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'f_mpiangona_adidy_annuel'
        unique_together = (('date', 'mpiangona', 'annee'),)
        db_table_comment = "Adidy isan-taona an'ny kristiana mpiangona sy mpikambana, t"


class LogFFgnRakitra(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=20)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    record_id = models.BigIntegerField(db_column='RECORD_ID', blank=True, null=True, db_comment="Identifiant unique an'ny rakitra tsirairay adika soratra")  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True, db_comment='Date/Andro nanaovana ny rakitra')  # Field name made lowercase.
    fidirana_laharana = models.CharField(db_column='FIDIRANA_LAHARANA', max_length=100, blank=True, null=True, db_comment='Fidirana voalohany, fidirana faharoa, sns.')  # Field name made lowercase.
    karazana_rakitra_id = models.BigIntegerField(db_column='KARAZANA_RAKITRA_ID', blank=True, null=True, db_comment="Karazan'ny rakitra natao")  # Field name made lowercase.
    montant = models.DecimalField(db_column='MONTANT', max_digits=20, decimal_places=2, blank=True, null=True, db_comment="Lelavola fitambaran'ny rakitra natao")  # Field name made lowercase.
    mpanome_vola_id = models.BigIntegerField(db_column='MPANOME_VOLA_ID', blank=True, null=True, db_comment="Identifiant an'ny mpiangona nanome vola (matetika raki-pisaorana)")  # Field name made lowercase.
    mpanome_vola_libelle = models.CharField(db_column='MPANOME_VOLA_LIBELLE', max_length=100, blank=True, null=True, db_comment="Anaran'ny mpanome ny vola rakitra (indrindra raha tsy mpiangona fa fikambanana na sampana)")  # Field name made lowercase.
    nomena_vola_id = models.BigIntegerField(db_column='NOMENA_VOLA_ID', blank=True, null=True, db_comment="Identifiant an'ny mpiangona nomena ny vola (ohatra : ny mpitandrina, olona hafa, sns.)")  # Field name made lowercase.
    nomena_vola_libelle = models.CharField(db_column='NOMENA_VOLA_LIBELLE', max_length=100, blank=True, null=True, db_comment="Anaran'ny nomena ny vola : indrindra raha tsy mpiangona fa fikambanana na sampana, na olona ivelan'ny fiangonana mihitsy.")  # Field name made lowercase.
    validation_code = models.CharField(db_column='VALIDATION_CODE', max_length=20, blank=True, null=True, db_comment='Code de validation, arakaraka ny dingana validation vita')  # Field name made lowercase.
    validateur1_code = models.CharField(db_column='VALIDATEUR1_CODE', max_length=20, blank=True, null=True, db_comment="Code an'ny validateur voalohany (mampiseho ny anarany fohy)")  # Field name made lowercase.
    validateur1_nom = models.CharField(db_column='VALIDATEUR1_NOM', max_length=200, blank=True, null=True, db_comment="Anarana lava, an'iny validateur voalohany")  # Field name made lowercase.
    validateur1_andraikitra = models.CharField(db_column='VALIDATEUR1_ANDRAIKITRA', max_length=255, blank=True, null=True, db_comment='Andraikitry ny validateur voalohany')  # Field name made lowercase.
    validateur2_code = models.CharField(db_column='VALIDATEUR2_CODE', max_length=20, blank=True, null=True, db_comment="Anarana fohy, an'ny validateur faharoa")  # Field name made lowercase.
    validateur2_nom = models.CharField(db_column='VALIDATEUR2_NOM', max_length=200, blank=True, null=True, db_comment="Anarana lava, an'ny validateur faharoa")  # Field name made lowercase.
    validateur2_andraikitra = models.CharField(db_column='VALIDATEUR2_ANDRAIKITRA', max_length=255, blank=True, null=True, db_comment='Andraikitry ny validateur faharoa')  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_f_fgn_rakitra'
        db_table_comment = 'Firaketana ny rakitra samihafa natao tao am-piangonana'


class LogFFgnVokatra(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    record_id = models.BigIntegerField(db_column='RECORD_ID', db_comment='Identifiant unique')  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True, db_comment='Date / andro nanatanterahana ny vokatra')  # Field name made lowercase.
    mpiangona_id = models.BigIntegerField(db_column='MPIANGONA_ID', blank=True, null=True, db_comment="Identifiant an'ny mpiangona nanao ny vokatra")  # Field name made lowercase.
    motif = models.CharField(db_column='MOTIF', max_length=100, blank=True, null=True, db_comment="Anton'ny vokatra / motif an'ilay fanomezana")  # Field name made lowercase.
    montant = models.DecimalField(db_column='MONTANT', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    omena_ny_fgn = models.SmallIntegerField(db_column='OMENA_NY_FGN', blank=True, null=True, db_comment='VRAI = Omena/atolotra ny fiangonana ilay vokatra (voka-dehibe) ; FAUX = atolotra ny Sampana na fikambanana na vondrona hafa ilay vola vokatra.')  # Field name made lowercase.
    beneficiaire_nom = models.CharField(db_column='BENEFICIAIRE_NOM', max_length=200, blank=True, null=True, db_comment="Anarana feno an'izay tolorana ny vokatra (ankoatra ny Fiangonana)")  # Field name made lowercase.
    validation_code = models.CharField(db_column='VALIDATION_CODE', max_length=20, blank=True, null=True, db_comment='Code de validation, arakaraka ny dingana validation vita')  # Field name made lowercase.
    validateur1_code = models.CharField(db_column='VALIDATEUR1_CODE', max_length=20, blank=True, null=True, db_comment="Code an'ny validateur voalohany (mampiseho ny anarany fohy)")  # Field name made lowercase.
    validateur1_nom = models.CharField(db_column='VALIDATEUR1_NOM', max_length=200, blank=True, null=True, db_comment="Anarana lava, an'iny validateur voalohany")  # Field name made lowercase.
    validateur1_andraikitra = models.CharField(db_column='VALIDATEUR1_ANDRAIKITRA', max_length=255, blank=True, null=True, db_comment='Andraikitry ny validateur voalohany')  # Field name made lowercase.
    validateur2_code = models.CharField(db_column='VALIDATEUR2_CODE', max_length=20, blank=True, null=True, db_comment="Code an'ny validateur faharoa (mampiseho ny anarany fohy)")  # Field name made lowercase.
    validateur2_nom = models.CharField(db_column='VALIDATEUR2_NOM', max_length=200, blank=True, null=True, db_comment="Anarana lava, an'iny validateur faharoa")  # Field name made lowercase.
    validateur2_andraikitra = models.CharField(db_column='VALIDATEUR2_ANDRAIKITRA', max_length=255, blank=True, null=True, db_comment='Andraikitry ny validateur faharoa')  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_f_fgn_vokatra'
        db_table_comment = 'Lisitry ny vokatra rehefa voaray'


class LogFMpandrayAdidyMensuel(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    record_id = models.BigIntegerField(db_column='RECORD_ID')  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    mpandray_id = models.BigIntegerField(db_column='MPANDRAY_ID', blank=True, null=True)  # Field name made lowercase.
    mois_code = models.CharField(db_column='MOIS_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    montant = models.DecimalField(db_column='MONTANT', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    validation_code = models.CharField(db_column='VALIDATION_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    validateur1_code = models.CharField(db_column='VALIDATEUR1_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    validateur1_nom = models.CharField(db_column='VALIDATEUR1_NOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    validateur1_andraikitra = models.CharField(db_column='VALIDATEUR1_ANDRAIKITRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    validateur2_code = models.CharField(db_column='VALIDATEUR2_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    validateur2_nom = models.CharField(db_column='VALIDATEUR2_NOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    validateur2_andraikitra = models.CharField(db_column='VALIDATEUR2_ANDRAIKITRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_f_mpandray_adidy_mensuel'
        db_table_comment = "Lisitry ny fandoavana Adidy isam-bolana an'ny Mpandray ny F"


class LogFMpiangonaAdidyAnnuel(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    record_id = models.BigIntegerField(db_column='RECORD_ID')  # Field name made lowercase.
    date = models.DateField(db_column='DATE', blank=True, null=True)  # Field name made lowercase.
    mpiangona_id = models.BigIntegerField(db_column='MPIANGONA_ID', blank=True, null=True)  # Field name made lowercase.
    annee = models.CharField(db_column='ANNEE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    montant = models.DecimalField(db_column='MONTANT', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    validation_code = models.CharField(db_column='VALIDATION_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    validateur1_code = models.CharField(db_column='VALIDATEUR1_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    validateur1_nom = models.CharField(db_column='VALIDATEUR1_NOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    validaetur1_andraiakitra = models.CharField(db_column='VALIDAETUR1_ANDRAIAKITRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    validateur2_code = models.CharField(db_column='VALIDATEUR2_CODE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    validateur2_nom = models.CharField(db_column='VALIDATEUR2_NOM', max_length=200, blank=True, null=True)  # Field name made lowercase.
    validateur2_andraikitra = models.CharField(db_column='VALIDATEUR2_ANDRAIKITRA', max_length=255, blank=True, null=True)  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_f_mpiangona_adidy_annuel'
        db_table_comment = "Adidy isan-taona an'ny kristiana mpiangona sy mpikambana, t"


class LogParBRubriques(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    rubrique = models.CharField(db_column='RUBRIQUE', max_length=20, db_comment="Code Rubrique an'ny Budget")  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=100, db_comment="Fiantsoana an'ilay Rubrique (ankoatra ny code)")  # Field name made lowercase.
    est_volamiditra = models.SmallIntegerField(db_column='EST_VOLAMIDITRA', db_comment='Oui/Vrai = vola miditra (recette). Raha tsy izay dia vola mivoaka (dépense).')  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='Enregistrement manan-kery.')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='VRAI = Aseho ; FAUX = afenina')  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_par_b_rubriques'
        db_table_comment = 'Paramètres de Budget - Rubriques dans le Budget'


class LogParBSousRubriques(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    srubrique = models.CharField(db_column='SRUBRIQUE', max_length=20, db_comment='Code de la sous-rubrique du budget')  # Field name made lowercase.
    rubrique = models.CharField(db_column='RUBRIQUE', max_length=20, db_comment='Code Rubrique associée')  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=100, db_comment='Fiantsoana ilay sous-rubrique (ankoatra ilay code)')  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='VRAI = Mbola manan-kery/ampiasaina ilay sous-rubrique')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='VRAI = aseho ilay enregistrement ; FAUX = afenina ilay enregistrement')  # Field name made lowercase.
    est_mensuel = models.SmallIntegerField(db_column='EST_MENSUEL', db_comment='VRAI = mouvement périodique/mensuel ; FAUX = mouvement tsy voatery misy miverimberina')  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_par_b_sous_rubriques'
        db_table_comment = 'Paramètres de Budget - Sous-Rubriques dans le Budget'


class LogParFKarazanaRakitra(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    record_id = models.BigIntegerField(db_column='RECORD_ID', db_comment="Identifiant unique pour plus de flexibilité de l'application")  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=20, db_comment="Code d'identification unique - an'ny karazana rakitra tsirairay")  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=100, db_comment="Libellé an'ny karazana rakitra")  # Field name made lowercase.
    srubrique = models.CharField(db_column='SRUBRIQUE', max_length=20, blank=True, null=True, db_comment='Sous-rubrique associée')  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='VRAI = mbola manankery/ampiasaina/misy ilay karazana rakitra')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='VRAI = aseho ilay enregistrement')  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_par_f_karazana_rakitra'
        db_table_comment = 'Paramètres de Budget/Finances - Karazana Rakitra ao am-piang'


class LogParFPeriodesMois(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=20)  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=100)  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE')  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_par_f_periodes_mois'
        db_table_comment = 'Périodes prédéfinies pour une meilleure organisation des don'


class LogParFValidateursVola(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=20, db_comment="Code d'identification unique du validateur")  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=200, db_comment="Anaran'ny mpanamarina ny vola")  # Field name made lowercase.
    andraikitra = models.CharField(db_column='ANDRAIKITRA', max_length=100, db_comment="Andraikitr'ilay mpanamarina ny vola")  # Field name made lowercase.
    mpiangona_id = models.BigIntegerField(db_column='MPIANGONA_ID', blank=True, null=True, db_comment="Identifiant unique amin'ny maha mpiangona")  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment="VRAI = mbola amperinasa amin'ny maha validateur io olona io")  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='VRAI = aseho ito enregistrement ito')  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_par_f_validateurs_vola'
        db_table_comment = 'Liste des validateurs potentiels'


class LogParFValidationCodes(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    code = models.CharField(db_column='CODE', max_length=20, db_comment="Code d'identification unique de validation")  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=100, db_comment="Fiantsoana an'ilay code de validation")  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='VRAI = mbola manan-kery (ampiasaina) ilay code de validation')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='VRAI = aseho ilay enregistrement')  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_par_f_validation_codes'
        db_table_comment = 'Codes de validation ampiasaina. Ohatra : VF = validation fin'


class LogTAdresses(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    record_id = models.BigIntegerField(db_column='RECORD_ID', blank=True, null=True, db_comment='Identification unique')  # Field name made lowercase.
    logement = models.CharField(db_column='LOGEMENT', max_length=255, blank=True, null=True, db_comment="Lot an'ny trano / numéro d'identification du logement")  # Field name made lowercase.
    repere = models.CharField(db_column='REPERE', max_length=255, blank=True, null=True, db_comment="Repère pour situer rapidement et efficacement l'adresse")  # Field name made lowercase.
    fgn_faritra_id = models.BigIntegerField(db_column='FGN_FARITRA_ID', blank=True, null=True, db_comment="Faritra misy an'ilay adresse")  # Field name made lowercase.
    fokontany_id = models.BigIntegerField(db_column='FOKONTANY_ID', blank=True, null=True, db_comment="Fokontany misy an'ilay adresse")  # Field name made lowercase.
    quartier_id = models.BigIntegerField(db_column='QUARTIER_ID', blank=True, null=True, db_comment="Quartier misy an'ilay adresse")  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT', db_comment="Date et heure de création de l'enregistrement (à des fins d'audit)")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_t_adresses'
        db_table_comment = "Lisitry ny adresses an'ny mpiangona sy ny mpikambana"


class LogTDiakonaMpiahyDtl(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    record_id = models.BigIntegerField(db_column='RECORD_ID', db_comment='Identifiant unique Equipe Diakona Mpiahy')  # Field name made lowercase.
    hdr_id = models.BigIntegerField(db_column='HDR_ID', blank=True, null=True, db_comment="Ekipa Diakona Mpiahy tompon'ny Détails")  # Field name made lowercase.
    diakona_id = models.BigIntegerField(db_column='DIAKONA_ID', blank=True, null=True, db_comment="Identifiant Ny Diakona tsirairay mandrafitra an'ilay Ekipa Mpiahy")  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True, db_comment="Fanazavazavana momba an'io Diakona Mpiahy iray mandrafitra ny ekipa io")  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='Flag / témoin - Manankery sa tsia ilay détail')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='Détail / Flag - Aseho sa tsia io détail io')  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT', db_comment="Date système de création de l'enregistrement (à des fins d'audit)")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_t_diakona_mpiahy_dtl'
        db_table_comment = 'Détails Equipe Diakona Mpiahy'


class LogTDiakonaMpiahyHdr(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    record_id = models.BigIntegerField(db_column='RECORD_ID', db_comment='Identifiant Unique de chaque équipe Diakona Mpiahy')  # Field name made lowercase.
    mandat = models.CharField(db_column='MANDAT', max_length=20, blank=True, null=True, db_comment="Taom-piasan'ny ekipa Diakona mpiahy (nanomboka oviana sy lany mandat rahoviana)")  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=100, blank=True, null=True, db_comment="Fiantsoana an'ilay ekipa Diakona Mpiahy. Ohatra : Fitambaran'ny anaran'ireo Diakona")  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='Témoin / Flag - Manankery sa tsia ilay Ekipa (atao FAUX/0 rehefa tapitra ny mandat)')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='Témoin / Flag - Aseho sa tsia ilay enregistrement')  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT', db_comment="Date système de création de l'enregistrement (à des fins d'audit)")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_t_diakona_mpiahy_hdr'
        db_table_comment = 'Lisitry ny Ekipa Diakona Mpiahy'


class LogTFoyers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    record_id = models.BigIntegerField(db_column='RECORD_ID')  # Field name made lowercase.
    numero = models.CharField(db_column='NUMERO', max_length=20, blank=True, null=True, db_comment='Laharana entina manisa ny tokantrano/ménage')  # Field name made lowercase.
    chef_id = models.BigIntegerField(db_column='CHEF_ID', blank=True, null=True, db_comment="ID an'izay mpiangona izay lohan'ny tokantrano (chef du foyer)")  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=100, blank=True, null=True, db_comment="Fiantsoana an'ilay tokantrano/ménage")  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='Témoin / flag - ahafantarana raha manankery na tsia ilay enregistrement')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='Témoin / Flag - ahafantarana na aseho na tsia ilay enregistrement')  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT', db_comment="Date de création de l'enregistrement (à des fins d'audit)")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_t_foyers'
        db_table_comment = "Lisitry ny tokantrano misy ao amin'ny fitandremana"


class LogTMpiangona(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    user_id = models.CharField(db_column='USER_ID', max_length=100)  # Field name made lowercase.
    action = models.CharField(db_column='ACTION', max_length=100)  # Field name made lowercase.
    table_name = models.CharField(db_column='TABLE_NAME', max_length=100)  # Field name made lowercase.
    record_id = models.BigIntegerField(db_column='RECORD_ID', db_comment="Identifiant unique an'ny mpiangona. Tokana ihany ny an'ny mpiangona tsirairay, ary tsy miova mihitsy na dia maty aza izy, na nifindra fiangonana, sns.")  # Field name made lowercase.
    numero = models.CharField(db_column='NUMERO', max_length=20, blank=True, null=True, db_comment="Numéro entin'ny fiangonana manavaka ny mpiangona sy ny mpikambana tsirairay. Tsy automatique.")  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=200, blank=True, null=True, db_comment='Nom de famille')  # Field name made lowercase.
    prenoms = models.CharField(db_column='PRENOMS', max_length=200, blank=True, null=True, db_comment="Fanampin'anarana. Raha tsisy afa tsy anarana fotsiny, dia avela banga ito.")  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True, db_comment="Fanazavana fanampiny momba ilay mpiangona. Ohatra : ny andraikitra manokana sahaniny (Ben'ny tanàna, Filohan'ny Fokontany Anona, PS SPAA12  taloha, PS SPAA12 Amperinasa, sns.)")  # Field name made lowercase.
    genre_id = models.BigIntegerField(db_column='GENRE_ID', blank=True, null=True, db_comment='Lahy sa vavy sa inona... Genre')  # Field name made lowercase.
    nationalite = models.CharField(db_column='NATIONALITE', max_length=100, blank=True, null=True, db_comment='Zom-pirenena')  # Field name made lowercase.
    foyer_id = models.BigIntegerField(db_column='FOYER_ID', blank=True, null=True, db_comment='Idenfiant Tokantrano/foyer/ménage misy ilay mpiangona na mpikambana')  # Field name made lowercase.
    date_naissance = models.DateField(db_column='DATE_NAISSANCE', blank=True, null=True, db_comment='Datinandro nahaterahana')  # Field name made lowercase.
    lieu_naissance = models.CharField(db_column='LIEU_NAISSANCE', max_length=100, blank=True, null=True, db_comment='Toerana nahaterahana')  # Field name made lowercase.
    pere_nom_complet = models.CharField(db_column='PERE_NOM_COMPLET', max_length=200, blank=True, null=True, db_comment='Nom complet du père')  # Field name made lowercase.
    pere_id = models.BigIntegerField(db_column='PERE_ID', blank=True, null=True, db_comment="Identifiant du père, raha mpiangona ao amin'ny fitandremana izy")  # Field name made lowercase.
    mere_nom_complet = models.CharField(db_column='MERE_NOM_COMPLET', max_length=200, blank=True, null=True, db_comment='Nom complet de la mère')  # Field name made lowercase.
    mere_id = models.BigIntegerField(db_column='MERE_ID', blank=True, null=True, db_comment="Identifiant de la mère, raha mpiangona ao amin'ny Fitandremana izy")  # Field name made lowercase.
    cin_id = models.CharField(db_column='CIN_ID', max_length=100, blank=True, null=True, db_comment='Laharana kara-panondrom-pirenena CIN')  # Field name made lowercase.
    cin_date = models.DateField(db_column='CIN_DATE', blank=True, null=True, db_comment='Date de délivrance de la CIN')  # Field name made lowercase.
    cin_lieu = models.CharField(db_column='CIN_LIEU', max_length=100, blank=True, null=True, db_comment='Lieu de délivrance de la CIN')  # Field name made lowercase.
    passeport_id = models.CharField(db_column='PASSEPORT_ID', max_length=100, blank=True, null=True, db_comment="Laharan'ny pasipaoro manan-kery naseho tamin'ny fotoana nanaovana ny enregistrement")  # Field name made lowercase.
    passeport_date = models.DateField(db_column='PASSEPORT_DATE', blank=True, null=True, db_comment='Date de délivrance du passeport')  # Field name made lowercase.
    passeport_lieu = models.CharField(db_column='PASSEPORT_LIEU', max_length=100, blank=True, null=True, db_comment='Lieu de délivrance du passeport')  # Field name made lowercase.
    tel1 = models.CharField(db_column='TEL1', max_length=20, blank=True, null=True, db_comment='Numéro téléphone, contact voalohany')  # Field name made lowercase.
    tel2 = models.CharField(db_column='TEL2', max_length=20, blank=True, null=True, db_comment='Numéro téléphone, contact faharoa')  # Field name made lowercase.
    sit_matr_id = models.BigIntegerField(db_column='SIT_MATR_ID', blank=True, null=True, db_comment='Situation matrimoniale : manambady, nisara-bady, maty vady, mpitovo, sns.')  # Field name made lowercase.
    profession = models.CharField(db_column='PROFESSION', max_length=100, blank=True, null=True, db_comment="Anton'asa")  # Field name made lowercase.
    fgn_taloha = models.CharField(db_column='FGN_TALOHA', max_length=100, blank=True, null=True, db_comment="Fiangonana nisy azy talohan'ny niaviany teto amin'ny Fitandremana. Ny anaran'ny fiangonana eto an-toerana ihany no atao eo raha efa teto foana izy hatry ny nahaterahany.")  # Field name made lowercase.
    adresse_id = models.BigIntegerField(db_column='ADRESSE_ID', blank=True, null=True, db_comment="Identifiant an'ny adresse misy ilay mpiangona na mpikambana")  # Field name made lowercase.
    faritra_id = models.BigIntegerField(db_column='FARITRA_ID', blank=True, null=True, db_comment='Vakim-paritra misy ilay mpiangona na mpikambana')  # Field name made lowercase.
    est_envie = models.SmallIntegerField(db_column='EST_ENVIE', db_comment='Mbola velona ve sa tsia ?')  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='Mbola manankery ve ito enregistrement ito ?')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment="Aseho ve (sa afenina) ito enregistrement ito ? Afenina no solon'ny suppression, fa tsy tokony hisy hofafaina mihitsy ny anarana nampidirina.")  # Field name made lowercase.
    est_vitabatisa = models.SmallIntegerField(db_column='EST_VITABATISA', db_comment="Efa vita batisa ve ? Raha efa mpandray, dia efa vita batisa izy izay (talohan'ny nandraisana azy ho mpandray ny Fanasan'ny Tompo)")  # Field name made lowercase.
    est_mpandray = models.SmallIntegerField(db_column='EST_MPANDRAY', db_comment="Efa mpandray ny Fanasan'ny Tompo ve ?")  # Field name made lowercase.
    est_suspendu = models.SmallIntegerField(db_column='EST_SUSPENDU', db_comment="Nahato amin'ny maha mpandray ny Fanasan'ny Tompo azy ve ? (na inona na inona mety ho antony) ")  # Field name made lowercase.
    est_zampielezana = models.SmallIntegerField(db_column='EST_ZAMPIELEZANA', db_comment='Zanaka am-pielezana ve ?')  # Field name made lowercase.
    est_mpiandry = models.SmallIntegerField(db_column='EST_MPIANDRY', db_comment='Mpiandry ve ?')  # Field name made lowercase.
    est_katekista = models.SmallIntegerField(db_column='EST_KATEKISTA', db_comment='Katekista ve ?')  # Field name made lowercase.
    est_mpitoriteny = models.SmallIntegerField(db_column='EST_MPITORITENY', db_comment='Mpitoriteny ve ?')  # Field name made lowercase.
    est_loholona = models.SmallIntegerField(db_column='EST_LOHOLONA', db_comment='Loholona ve ?')  # Field name made lowercase.
    est_diakona = models.SmallIntegerField(db_column='EST_DIAKONA', db_comment='Diakona ve ?')  # Field name made lowercase.
    est_mpitandrina = models.SmallIntegerField(db_column='EST_MPITANDRINA', db_comment='Mpitandrina ve ?')  # Field name made lowercase.
    est_nympitandrina = models.SmallIntegerField(db_column='EST_NYMPITANDRINA', db_comment='Ny Mpitandrina amperinasa ve ?')  # Field name made lowercase.
    est_stagiaire = models.SmallIntegerField(db_column='EST_STAGIAIRE', db_comment='Mpitandrina miza-draharaha mandritra ny fotoana voafetra ve ?')  # Field name made lowercase.
    stage_periode = models.CharField(db_column='STAGE_PERIODE', max_length=255, blank=True, null=True, db_comment="Période de stage natao tao amin'ny fitandremana, raha efa nanao fizaran-draharaha amin'ny maha Mpitandrina, tao. Raha tsy izay, dia tsy fenoina io.")  # Field name made lowercase.
    dkn_mpiahy_id = models.BigIntegerField(db_column='DKN_MPIAHY_ID', blank=True, null=True, db_comment="Identifiant an'ny Ekipa Diakona Mpiahy azy")  # Field name made lowercase.
    changed_at = models.DateTimeField(db_column='CHANGED_AT', db_comment="Date système de création de cet enregistrement (à des fins d'audit)")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log_t_mpiangona'
        db_table_comment = 'Lisitry ny mpiangona sy ny mpikambana'


class ParBRubriques(models.Model):
    rubrique = models.CharField(db_column='RUBRIQUE', primary_key=True, max_length=20, db_comment="Code Rubrique an'ny Budget")  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', unique=True, max_length=100, db_comment="Fiantsoana an'ilay Rubrique (ankoatra ny code)")  # Field name made lowercase.
    est_volamiditra = models.SmallIntegerField(db_column='EST_VOLAMIDITRA', db_comment='Oui/Vrai = vola miditra (recette). Raha tsy izay dia vola mivoaka (dépense).')  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='Enregistrement manan-kery.')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='VRAI = Aseho ; FAUX = afenina')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'par_b_rubriques'
        db_table_comment = 'Paramètres de Budget - Rubriques dans le Budget'


class ParBSousRubriques(models.Model):
    srubrique = models.CharField(db_column='SRUBRIQUE', primary_key=True, max_length=20, db_comment='Code de la sous-rubrique du budget')  # Field name made lowercase.
    rubrique = models.ForeignKey(ParBRubriques, models.DO_NOTHING, db_column='RUBRIQUE', db_comment='Code Rubrique associée')  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', unique=True, max_length=100, db_comment='Fiantsoana ilay sous-rubrique (ankoatra ilay code)')  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='VRAI = Mbola manan-kery/ampiasaina ilay sous-rubrique')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='VRAI = aseho ilay enregistrement ; FAUX = afenina ilay enregistrement')  # Field name made lowercase.
    est_mensuel = models.SmallIntegerField(db_column='EST_MENSUEL', db_comment='VRAI = mouvement périodique/mensuel ; FAUX = mouvement tsy voatery misy miverimberina')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'par_b_sous_rubriques'
        db_table_comment = 'Paramètres de Budget - Sous-Rubriques dans le Budget'


class ParFKarazanaRakitra(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment="Identifiant unique pour plus de flexibilité de l'application")  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=20, db_comment="Code d'identification unique - an'ny karazana rakitra tsirairay")  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', unique=True, max_length=100, db_comment="Libellé an'ny karazana rakitra")  # Field name made lowercase.
    srubrique = models.ForeignKey(ParBSousRubriques, models.DO_NOTHING, db_column='SRUBRIQUE', blank=True, null=True, db_comment='Sous-rubrique associée')  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='VRAI = mbola manankery/ampiasaina/misy ilay karazana rakitra')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='VRAI = aseho ilay enregistrement')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'par_f_karazana_rakitra'
        db_table_comment = 'Paramètres de Budget/Finances - Karazana Rakitra ao am-piang'


class ParFPeriodesMois(models.Model):
    code = models.CharField(db_column='CODE', primary_key=True, max_length=20)  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', unique=True, max_length=100)  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE')  # Field name made lowercase.
    change_at = models.DateTimeField(db_column='CHANGE_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'par_f_periodes_mois'
        db_table_comment = 'Périodes prédéfinies pour une meilleure organisation des don'


class ParFValidateursVola(models.Model):
    code = models.CharField(db_column='CODE', primary_key=True, max_length=20, db_comment="Code d'identification unique du validateur")  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=200, db_comment="Anaran'ny mpanamarina ny vola")  # Field name made lowercase.
    andraikitra = models.CharField(db_column='ANDRAIKITRA', max_length=100, db_comment="Andraikitr'ilay mpanamarina ny vola")  # Field name made lowercase.
    mpiangona_id = models.BigIntegerField(db_column='MPIANGONA_ID', blank=True, null=True, db_comment="Identifiant unique amin'ny maha mpiangona")  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment="VRAI = mbola amperinasa amin'ny maha validateur io olona io")  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='VRAI = aseho ito enregistrement ito')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'par_f_validateurs_vola'
        unique_together = (('mpiangona_id', 'andraikitra'), ('nom', 'andraikitra'),)
        db_table_comment = 'Liste des validateurs potentiels'


class ParFValidationCodes(models.Model):
    code = models.CharField(db_column='CODE', primary_key=True, max_length=20, db_comment="Code d'identification unique de validation")  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', unique=True, max_length=100, db_comment="Fiantsoana an'ilay code de validation")  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='VRAI = mbola manan-kery (ampiasaina) ilay code de validation')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='VRAI = aseho ilay enregistrement')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'par_f_validation_codes'
        db_table_comment = 'Codes de validation ampiasaina. Ohatra : VF = validation fin'


class ParFgnFaritra(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment='Identifiant Unique')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=20, db_comment="Code unique an'ny faritra an'ny fiangonana")  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=100, db_comment="Fiantsoana an'ilay vakim-paritra an'ny fiangonana")  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True, db_comment="Fanazavazavana an'ilay vakim-paritra an'ny fiangonana")  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'par_fgn_faritra'
        db_table_comment = "Vakim-paritra eo amin'ny Fitandremana"


class ParGenres(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment='Identifiant Unique')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=20, db_comment="Code d'identification unique du genre")  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=100, db_comment="Fiantsoana fohy an'ilay genre")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'par_genres'
        db_table_comment = "Genres an'ny mpiangona sy ny mpikambana"


class ParGeoCommunes(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment='Identifiant Unique')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=20, db_comment="Code d'identification unique de la commune")  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=100, db_comment='Nom complet de la commune')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'par_geo_communes'
        db_table_comment = 'Communes misy ireo mpiangona sy mpikambana'


class ParGeoFokontany(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment='Identification unique')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=20, db_comment="Code d'identification unique du Fokontany")  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=100, db_comment='Nom complet du Fokontany')  # Field name made lowercase.
    commune = models.ForeignKey(ParGeoCommunes, models.DO_NOTHING, db_column='COMMUNE_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'par_geo_fokontany'
        db_table_comment = 'Fokontany samihafa misy ny mpiangona sy ny mpikambana'


class ParGeoQuartiers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment='Identification Unique du Quartier')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=20, db_comment="Code d'identification unique du Quartier")  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=100, db_comment='Nom complet du Quartier')  # Field name made lowercase.
    fokontany = models.ForeignKey(ParGeoFokontany, models.DO_NOTHING, db_column='FOKONTANY_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'par_geo_quartiers'
        db_table_comment = 'Quartiers misy ireo mpiangona sy mpikambana'


class ParSitMatr(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment='Identification Unique')  # Field name made lowercase.
    code = models.CharField(db_column='CODE', unique=True, max_length=20, db_comment="Code d'identification unique de la situation matrimoniale")  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=100, db_comment="Fiantsoana an'ilay situation matrimoniale")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'par_sit_matr'
        db_table_comment = "Situation matrimoniale an'ny mpiangona sy mpikambana"


class TAdresses(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment='Identification unique')  # Field name made lowercase.
    logement = models.CharField(db_column='LOGEMENT', unique=True, max_length=255, db_comment="Lot an'ny trano / numéro d'identification du logement")  # Field name made lowercase.
    repere = models.CharField(db_column='REPERE', max_length=255, blank=True, null=True, db_comment="Repère pour situer rapidement et efficacement l'adresse")  # Field name made lowercase.
    fgn_faritra = models.ForeignKey(ParFgnFaritra, models.DO_NOTHING, db_column='FGN_FARITRA_ID', blank=True, null=True, db_comment="Faritra misy an'ilay adresse")  # Field name made lowercase.
    fokontany = models.ForeignKey(ParGeoFokontany, models.DO_NOTHING, db_column='FOKONTANY_ID', blank=True, null=True, db_comment="Fokontany misy an'ilay adresse")  # Field name made lowercase.
    quartier = models.ForeignKey(ParGeoQuartiers, models.DO_NOTHING, db_column='QUARTIER_ID', blank=True, null=True, db_comment="Quartier misy an'ilay adresse")  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', db_comment="Date et heure de création de l'enregistrement (à des fins d'audit)")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_adresses'
        db_table_comment = "Lisitry ny adresses an'ny mpiangona sy ny mpikambana"


class TDiakonaMpiahyDtl(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment='Identifiant unique Equipe Diakona Mpiahy')  # Field name made lowercase.
    hdr = models.ForeignKey('TDiakonaMpiahyHdr', models.DO_NOTHING, db_column='HDR_ID', db_comment="Ekipa Diakona Mpiahy tompon'ny Détails")  # Field name made lowercase.
    diakona_id = models.BigIntegerField(db_column='DIAKONA_ID', db_comment="Identifiant Ny Diakona tsirairay mandrafitra an'ilay Ekipa Mpiahy")  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True, db_comment="Fanazavazavana momba an'io Diakona Mpiahy iray mandrafitra ny ekipa io")  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='Flag / témoin - Manankery sa tsia ilay détail')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='Détail / Flag - Aseho sa tsia io détail io')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', db_comment="Date système de création de l'enregistrement (à des fins d'audit)")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_diakona_mpiahy_dtl'
        unique_together = (('hdr', 'diakona_id'),)
        db_table_comment = 'Détails Equipe Diakona Mpiahy'


class TDiakonaMpiahyHdr(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment='Identifiant Unique de chaque équipe Diakona Mpiahy')  # Field name made lowercase.
    mandat = models.CharField(db_column='MANDAT', max_length=20, db_comment="Taom-piasan'ny ekipa Diakona mpiahy (nanomboka oviana sy lany mandat rahoviana)")  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', max_length=100, db_comment="Fiantsoana an'ilay ekipa Diakona Mpiahy. Ohatra : Fitambaran'ny anaran'ireo Diakona")  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='Témoin / Flag - Manankery sa tsia ilay Ekipa (atao FAUX/0 rehefa tapitra ny mandat)')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='Témoin / Flag - Aseho sa tsia ilay enregistrement')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', db_comment="Date système de création de l'enregistrement (à des fins d'audit)")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_diakona_mpiahy_hdr'
        unique_together = (('mandat', 'libelle'),)
        db_table_comment = 'Lisitry ny Ekipa Diakona Mpiahy'


class TFoyers(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    numero = models.CharField(db_column='NUMERO', unique=True, max_length=20, blank=True, null=True, db_comment='Laharana entina manisa ny tokantrano/ménage')  # Field name made lowercase.
    chef_id = models.BigIntegerField(db_column='CHEF_ID', unique=True, blank=True, null=True, db_comment="ID an'izay mpiangona izay lohan'ny tokantrano (chef du foyer)")  # Field name made lowercase.
    libelle = models.CharField(db_column='LIBELLE', unique=True, max_length=100, db_comment="Fiantsoana an'ilay tokantrano/ménage")  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='Témoin / flag - ahafantarana raha manankery na tsia ilay enregistrement')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment='Témoin / Flag - ahafantarana na aseho na tsia ilay enregistrement')  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', db_comment="Date de création de l'enregistrement (à des fins d'audit)")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_foyers'
        db_table_comment = "Lisitry ny tokantrano misy ao amin'ny fitandremana"


class TMpiangona(models.Model):
    id = models.BigAutoField(db_column='ID', primary_key=True, db_comment="Identifiant unique an'ny mpiangona. Tokana ihany ny an'ny mpiangona tsirairay, ary tsy miova mihitsy na dia maty aza izy, na nifindra fiangonana, sns.")  # Field name made lowercase.
    numero = models.CharField(db_column='NUMERO', unique=True, max_length=20, blank=True, null=True, db_comment="Numéro entin'ny fiangonana manavaka ny mpiangona sy ny mpikambana tsirairay. Tsy automatique.")  # Field name made lowercase.
    nom = models.CharField(db_column='NOM', max_length=200, db_comment='Nom de famille')  # Field name made lowercase.
    prenoms = models.CharField(db_column='PRENOMS', max_length=200, blank=True, null=True, db_comment="Fanampin'anarana. Raha tsisy afa tsy anarana fotsiny, dia avela banga ito.")  # Field name made lowercase.
    description = models.CharField(db_column='DESCRIPTION', max_length=255, blank=True, null=True, db_comment="Fanazavana fanampiny momba ilay mpiangona. Ohatra : ny andraikitra manokana sahaniny (Ben'ny tanàna, Filohan'ny Fokontany Anona, PS SPAA12  taloha, PS SPAA12 Amperinasa, sns.)")  # Field name made lowercase.
    genre = models.ForeignKey(ParGenres, models.DO_NOTHING, db_column='GENRE_ID', blank=True, null=True, db_comment='Lahy sa vavy sa inona... Genre')  # Field name made lowercase.
    nationalite = models.CharField(db_column='NATIONALITE', max_length=100, db_comment='Zom-pirenena')  # Field name made lowercase.
    foyer = models.ForeignKey(TFoyers, models.DO_NOTHING, db_column='FOYER_ID', blank=True, null=True, db_comment='Idenfiant Tokantrano/foyer/ménage misy ilay mpiangona na mpikambana')  # Field name made lowercase.
    date_naissance = models.DateField(db_column='DATE_NAISSANCE', blank=True, null=True, db_comment='Datinandro nahaterahana')  # Field name made lowercase.
    lieu_naissance = models.CharField(db_column='LIEU_NAISSANCE', max_length=100, blank=True, null=True, db_comment='Toerana nahaterahana')  # Field name made lowercase.
    pere_nom_complet = models.CharField(db_column='PERE_NOM_COMPLET', max_length=200, blank=True, null=True, db_comment='Nom complet du père')  # Field name made lowercase.
    pere = models.ForeignKey('self', models.DO_NOTHING, db_column='PERE_ID', blank=True, null=True, db_comment="Identifiant du père, raha mpiangona ao amin'ny fitandremana izy")  # Field name made lowercase.
    mere_nom_complet = models.CharField(db_column='MERE_NOM_COMPLET', max_length=200, blank=True, null=True, db_comment='Nom complet de la mère')  # Field name made lowercase.
    mere = models.ForeignKey('self', models.DO_NOTHING, db_column='MERE_ID', related_name='tmpiangona_mere_set', blank=True, null=True, db_comment="Identifiant de la mère, raha mpiangona ao amin'ny Fitandremana izy")  # Field name made lowercase.
    cin_id = models.CharField(db_column='CIN_ID', unique=True, max_length=100, blank=True, null=True, db_comment='Laharana kara-panondrom-pirenena CIN')  # Field name made lowercase.
    cin_date = models.DateField(db_column='CIN_DATE', blank=True, null=True, db_comment='Date de délivrance de la CIN')  # Field name made lowercase.
    cin_lieu = models.CharField(db_column='CIN_LIEU', max_length=100, blank=True, null=True, db_comment='Lieu de délivrance de la CIN')  # Field name made lowercase.
    passeport_id = models.CharField(db_column='PASSEPORT_ID', unique=True, max_length=100, blank=True, null=True, db_comment="Laharan'ny pasipaoro manan-kery naseho tamin'ny fotoana nanaovana ny enregistrement")  # Field name made lowercase.
    passeport_date = models.DateField(db_column='PASSEPORT_DATE', blank=True, null=True, db_comment='Date de délivrance du passeport')  # Field name made lowercase.
    passeport_lieu = models.CharField(db_column='PASSEPORT_LIEU', max_length=100, blank=True, null=True, db_comment='Lieu de délivrance du passeport')  # Field name made lowercase.
    tel1 = models.CharField(db_column='TEL1', max_length=20, blank=True, null=True, db_comment='Numéro téléphone, contact voalohany')  # Field name made lowercase.
    tel2 = models.CharField(db_column='TEL2', max_length=20, blank=True, null=True, db_comment='Numéro téléphone, contact faharoa')  # Field name made lowercase.
    sit_matr = models.ForeignKey(ParSitMatr, models.DO_NOTHING, db_column='SIT_MATR_ID', blank=True, null=True, db_comment='Situation matrimoniale : manambady, nisara-bady, maty vady, mpitovo, sns.')  # Field name made lowercase.
    profession = models.CharField(db_column='PROFESSION', max_length=100, blank=True, null=True, db_comment="Anton'asa")  # Field name made lowercase.
    fgn_taloha = models.CharField(db_column='FGN_TALOHA', max_length=100, blank=True, null=True, db_comment="Fiangonana nisy azy talohan'ny niaviany teto amin'ny Fitandremana. Ny anaran'ny fiangonana eto an-toerana ihany no atao eo raha efa teto foana izy hatry ny nahaterahany.")  # Field name made lowercase.
    adresse = models.ForeignKey(TAdresses, models.DO_NOTHING, db_column='ADRESSE_ID', blank=True, null=True, db_comment="Identifiant an'ny adresse misy ilay mpiangona na mpikambana")  # Field name made lowercase.
    faritra = models.ForeignKey(ParFgnFaritra, models.DO_NOTHING, db_column='FARITRA_ID', blank=True, null=True, db_comment='Vakim-paritra misy ilay mpiangona na mpikambana')  # Field name made lowercase.
    est_envie = models.SmallIntegerField(db_column='EST_ENVIE', db_comment='Mbola velona ve sa tsia ?')  # Field name made lowercase.
    est_actif = models.SmallIntegerField(db_column='EST_ACTIF', db_comment='Mbola manankery ve ito enregistrement ito ?')  # Field name made lowercase.
    est_visible = models.SmallIntegerField(db_column='EST_VISIBLE', db_comment="Aseho ve (sa afenina) ito enregistrement ito ? Afenina no solon'ny suppression, fa tsy tokony hisy hofafaina mihitsy ny anarana nampidirina.")  # Field name made lowercase.
    est_vitabatisa = models.SmallIntegerField(db_column='EST_VITABATISA', db_comment="Efa vita batisa ve ? Raha efa mpandray, dia efa vita batisa izy izay (talohan'ny nandraisana azy ho mpandray ny Fanasan'ny Tompo)")  # Field name made lowercase.
    est_mpandray = models.SmallIntegerField(db_column='EST_MPANDRAY', db_comment="Efa mpandray ny Fanasan'ny Tompo ve ?")  # Field name made lowercase.
    est_suspendu = models.SmallIntegerField(db_column='EST_SUSPENDU', db_comment="Nahato amin'ny maha mpandray ny Fanasan'ny Tompo azy ve ? (na inona na inona mety ho antony) ")  # Field name made lowercase.
    est_zampielezana = models.SmallIntegerField(db_column='EST_ZAMPIELEZANA', db_comment='Zanaka am-pielezana ve ?')  # Field name made lowercase.
    est_mpiandry = models.SmallIntegerField(db_column='EST_MPIANDRY', db_comment='Mpiandry ve ?')  # Field name made lowercase.
    est_katekista = models.SmallIntegerField(db_column='EST_KATEKISTA', db_comment='Katekista ve ?')  # Field name made lowercase.
    est_mpitoriteny = models.SmallIntegerField(db_column='EST_MPITORITENY', db_comment='Mpitoriteny ve ?')  # Field name made lowercase.
    est_loholona = models.SmallIntegerField(db_column='EST_LOHOLONA', db_comment='Loholona ve ?')  # Field name made lowercase.
    est_diakona = models.SmallIntegerField(db_column='EST_DIAKONA', db_comment='Diakona ve ?')  # Field name made lowercase.
    est_mpitandrina = models.SmallIntegerField(db_column='EST_MPITANDRINA', db_comment='Mpitandrina ve ?')  # Field name made lowercase.
    est_nympitandrina = models.SmallIntegerField(db_column='EST_NYMPITANDRINA', db_comment='Ny Mpitandrina amperinasa ve ?')  # Field name made lowercase.
    est_stagiaire = models.SmallIntegerField(db_column='EST_STAGIAIRE', db_comment='Mpitandrina miza-draharaha mandritra ny fotoana voafetra ve ?')  # Field name made lowercase.
    stage_periode = models.CharField(db_column='STAGE_PERIODE', max_length=255, blank=True, null=True, db_comment="Période de stage natao tao amin'ny fitandremana, raha efa nanao fizaran-draharaha amin'ny maha Mpitandrina, tao. Raha tsy izay, dia tsy fenoina io.")  # Field name made lowercase.
    dkn_mpiahy = models.ForeignKey(TDiakonaMpiahyHdr, models.DO_NOTHING, db_column='DKN_MPIAHY_ID', blank=True, null=True, db_comment="Identifiant an'ny Ekipa Diakona Mpiahy azy (HDR_ID)")  # Field name made lowercase.
    created_at = models.DateTimeField(db_column='CREATED_AT', db_comment="Date système de création de cet enregistrement (à des fins d'audit)")  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 't_mpiangona'
        unique_together = (('nom', 'prenoms'),)
        db_table_comment = 'Lisitry ny mpiangona sy ny mpikambana'
