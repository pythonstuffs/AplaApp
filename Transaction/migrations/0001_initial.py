# Generated by Django 3.2.4 on 2022-02-20 09:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Product', '0001_initial'),
        ('BusinessOwener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('TID', models.BigAutoField(primary_key=True, serialize=False)),
                ('BName', models.CharField(max_length=30)),
                ('TotalPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TransactionDate', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('BID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BusinessOwener.storeprofile')),
                ('CID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentStatus',
            fields=[
                ('name', models.CharField(max_length=30)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('last_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionMode',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionStatus',
            fields=[
                ('created', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=30)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('PName', models.CharField(max_length=30)),
                ('OID', models.BigAutoField(primary_key=True, serialize=False)),
                ('PUnit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PPrice', models.DecimalField(decimal_places=2, max_digits=10)),
                ('PTotal', models.DecimalField(decimal_places=2, max_digits=10)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('PID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Product.product')),
                ('TID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transaction.invoice')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='PTransactionMode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transaction.transactionmode'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='PaymentStatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transaction.paymentstatus'),
        ),
        migrations.AddField(
            model_name='invoice',
            name='TransactionStatus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Transaction.transactionstatus'),
        ),
    ]
