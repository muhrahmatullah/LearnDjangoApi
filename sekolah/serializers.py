from rest_framework import serializers

from sekolah.models import Siswa, OrangTuaSiswa, Guru


class GuruSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nama = serializers.CharField(required=True, allow_blank=False, max_length=100)
    PEREMPUAN = 'P'
    LAKI_LAKI = 'L'
    PILIHAN_JENIS_KELAMIN = (
        (PEREMPUAN, 'Perempuan'),
        (LAKI_LAKI, 'Laki-laki')
    )
    jeniskelamin = serializers.ChoiceField(choices=PILIHAN_JENIS_KELAMIN, default=PEREMPUAN)

    def create(self, validated_data):
        """
        Create and return a new `Guru` instance, given the validated data.
        """
        return Guru.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Guru` instance, given the validated data.
        """
        instance.nama = validated_data.get('nama', instance.nama)
        instance.jeniskelamin = validated_data.get('jeniskelamin', instance.jeniskelamin)
        instance.save()
        return instance
class OrangTuaSiswaSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrangTuaSiswa
        fields = ('id', 'namaayah', 'namaibu')


class SiswaSerializer(serializers.ModelSerializer):
    orangtua = OrangTuaSiswaSerializer(read_only=True)  # if not read_only, implement .create() to handle nested
    class Meta:
        model = Siswa
        fields = ('id', 'nama', 'tanggallahir', 'jeniskelamin', 'orangtua')