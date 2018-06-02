# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Siswa(models.Model):
    nama = models.CharField(max_length=100)
    tanggallahir = models.DateField()
    PEREMPUAN = 'P'
    LAKI_LAKI = 'L'
    PILIHAN_JENIS_KELAMIN = (
        (PEREMPUAN, 'Perempuan'),
        (LAKI_LAKI, 'Laki-laki')
    )
    jeniskelamin = models.CharField(max_length=1, choices=PILIHAN_JENIS_KELAMIN, default=PEREMPUAN)

    def __str__(self):
        return '#{} {}'.format(self.id, self.nama)
#@title class Guru
class Guru(models.Model):
    nama = models.CharField(max_length=100)
    PEREMPUAN = 'P'
    LAKI_LAKI = 'L'
    PILIHAN_JENIS_KELAMIN = (
        (PEREMPUAN, 'Perempuan'),
        (LAKI_LAKI, 'Laki-laki')
    )
    jeniskelamin = models.CharField(max_length=1,
                                    choices=PILIHAN_JENIS_KELAMIN,
                                    default=PEREMPUAN)

    def __str__(self):
        return '{} {}' \
            .format('Bu' if self.jeniskelamin == self.PEREMPUAN else 'Pak',
                    self.nama)

#@title class Pelajaran (revision with ForeignKey)
class Pelajaran(models.Model):
    nama = models.CharField(max_length=100)
    pengajar = models.ForeignKey(to=Guru, on_delete=models.CASCADE)

    def __str__(self):
        return '{} oleh {}'.format(self.nama, self.pengajar)
class OrangTuaSiswa(models.Model):
    namaayah = models.CharField(max_length=100)
    namaibu = models.CharField(max_length=100)

    def __str__(self):
        return 'ayah: {}  ibu: {}'.format(self.namaayah, self.namaibu)
