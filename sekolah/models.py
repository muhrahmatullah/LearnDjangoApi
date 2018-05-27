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