# Generated by Django 4.1.3 on 2022-12-11 22:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_types', models.CharField(max_length=100, null=True)),
                ('country', models.CharField(max_length=25)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('mat_id', models.IntegerField(unique=True)),
                ('entry_date', models.DateField(auto_now_add=True)),
                ('source', models.CharField(max_length=150)),
                ('designation', models.CharField(max_length=50)),
                ('heat_treatment', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialCategory1',
            fields=[
                ('category', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='MaterialCategory2',
            fields=[
                ('category', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('upper_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mid_categories', to='API_Materials.materialcategory1')),
            ],
        ),
        migrations.CreateModel(
            name='MechanicalProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tensile_strength', models.IntegerField(null=True)),
                ('thermal_conductivity', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('reduction_of_area', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('cyclic_yield_strength', models.IntegerField(null=True)),
                ('elastic_modulus', models.JSONField(null=True)),
                ('poissons_ratio', models.JSONField(null=True)),
                ('shear_modulus', models.JSONField(null=True)),
                ('yield_strength', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhysicalProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chemical_composition', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('DIC_params', models.JSONField()),
                ('thermog_params', models.JSONField(null=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tests', to='API_Materials.material')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tests', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ThermalProperties',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thermal_expansion_coef', models.JSONField(null=True)),
                ('specific_heat_capacity', models.JSONField(null=True)),
                ('thermal_conductivity', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Laboratory',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API_Materials.entity')),
            ],
            bases=('API_Materials.entity',),
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('entity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='API_Materials.entity')),
                ('applications', models.CharField(max_length=100, null=True)),
                ('year_founded', models.IntegerField()),
                ('patents', models.CharField(max_length=250)),
                ('certifications', models.CharField(max_length=250)),
            ],
            bases=('API_Materials.entity',),
        ),
        migrations.CreateModel(
            name='ThermogStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_num', models.IntegerField()),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_Materials.test')),
            ],
        ),
        migrations.CreateModel(
            name='ThermogDatapoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_Materials.thermogstage')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('equation', models.CharField(max_length=50)),
                ('parameters', models.JSONField()),
                ('parametersKPI', models.JSONField()),
                ('model_file', models.FileField(upload_to='')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_Materials.material')),
            ],
        ),
        migrations.CreateModel(
            name='MaterialCategory3',
            fields=[
                ('category', models.CharField(max_length=25, primary_key=True, serialize=False, unique=True)),
                ('upper_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lower_categories', to='API_Materials.materialcategory2')),
            ],
        ),
        migrations.AddField(
            model_name='material',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='materials', to='API_Materials.materialcategory3'),
        ),
        migrations.AddField(
            model_name='material',
            name='mechanical_properties',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='API_Materials.mechanicalproperties'),
        ),
        migrations.AddField(
            model_name='material',
            name='physical_properties',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='API_Materials.physicalproperties'),
        ),
        migrations.AddField(
            model_name='material',
            name='submitted_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='materials', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='material',
            name='thermal_properties',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='API_Materials.thermalproperties'),
        ),
        migrations.CreateModel(
            name='DICStage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stage_num', models.IntegerField()),
                ('timestamp_undef', models.DecimalField(decimal_places=6, max_digits=10)),
                ('timestamp_def', models.DecimalField(decimal_places=6, max_digits=10)),
                ('ambient_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('load', models.DecimalField(decimal_places=2, max_digits=5)),
                ('test', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_Materials.test')),
            ],
        ),
        migrations.CreateModel(
            name='DICDatapoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_x', models.IntegerField()),
                ('index_y', models.IntegerField()),
                ('x', models.DecimalField(decimal_places=6, max_digits=8)),
                ('y', models.DecimalField(decimal_places=6, max_digits=8)),
                ('z', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('displacement_x', models.DecimalField(decimal_places=6, max_digits=8)),
                ('displacement_y', models.DecimalField(decimal_places=6, max_digits=8)),
                ('displacement_z', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('strain_x', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('strain_y', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('strain_major', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('strain_minor', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('thickness_reduction', models.DecimalField(decimal_places=6, max_digits=8, null=True)),
                ('stage', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_Materials.dicstage')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('postal_code', models.CharField(max_length=25)),
                ('street', models.CharField(max_length=100)),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API_Materials.supplier')),
            ],
        ),
    ]