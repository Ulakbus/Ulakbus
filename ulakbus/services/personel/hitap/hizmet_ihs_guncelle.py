# -*-  coding: utf-8 -*-
"""
"""

# Copyright (C) 2015 ZetaOps Inc.
#
# This file is licensed under the GNU General Public License v3
# (GPLv3).  See LICENSE.txt for details.

"""HITAP IHS Guncelle

Hitap'a personelin IHS bilgilerinin guncellemesini yapar.

"""

__author__ = 'H.İbrahim Yılmaz (drlinux)'

from ulakbus.services.personel.hitap.hitap_guncelle import HITAPGuncelle
from ulakbus.models.hitap import HizmetIHS


class HizmetIhsUpdate(HITAPGuncelle):
    """
    HITAP Ekleme servisinden kalıtılmış Hizmet IHS Bilgisi Guncelleme servisi

    """

    def handle(self):
        """Servis çağrıldığında tetiklenen metod.

        Attributes:
            service_name (str): İlgili Hitap sorgu servisinin adı
            service_dict (dict): ''HizmetIHS'' modelinden gelen kayıtların alanları,
                    HizmetIHSUpdate servisinin alanlarıyla eşlenmektedir.
                    Filtreden geçecek tarih alanları listede tutulmaktadır.
        """
        key = self.request.payload['key']

        self.service_name = 'HizmetIHSUpdate'
        self.service_dict = {
            'fields': {
                'ihzID':self.request.payload['kayit_no'],
                'tckn': self.request.payload['tckn'],
                'baslamaTarihi': self.request.payload['baslama_tarihi'],
                'bitisTarihi': self.request.payload['bitis_tarihi'],
                'ihzNevi': self.request.payload['ihz_nevi'],
            },
            'date_filter': ['baslamaTarihi', 'bitisTarihi'],
            'required_fields': ['tckn', 'ihzID', 'baslamaTarihi', 'bitisTarihi', 'ihzNevi']
        }
        super(HizmetIhsUpdate, self).handle()
