# -*- coding:utf-8 -*-
from plone import api
from plone.i18n.normalizer import idnormalizer
from Products.Five.browser import BrowserView
from requests.exceptions import ConnectionError
from requests.exceptions import HTTPError

import requests

sedes = {
    'C.U.': 'cu',
    'Cuernavaca': 'cuernavaca',
    'Juriquilla': 'juriquilla',
    'Oaxaca': 'oaxaca',
}


class PFGrestView(BrowserView):
    """View that send request to Plaza Prometo."""

    def __init__(self, context, request):
        """Initialize view."""
        self.context = context
        self.request = request

    def __call__(self):
        self.call_restapi()
        return self.index()

    def call_restapi(self):
        """Go to plaza prometeo site"""
        portal = api.portal.get()
        fsdobj = portal['fsd'][api.user.get_current().id]
        days = []
        if self.request.form['ninguno']:
            days.append('Ninguno')
        if self.request.form['lunes']:
            days.append('Lunes')
        if self.request.form['martes']:
            days.append('Martes')
        if self.request.form['miercoles']:
            days.append('Miercoles')
        if self.request.form['jueves']:
            days.append('Jueves')
        if self.request.form['no-se']:
            days.append('No se')
        data = {
            '@type': 'imparticipant',
            'firstname': fsdobj.firstName,
            'lastname': fsdobj.lastName,
            'campus': sedes[fsdobj.sede],
            'email': fsdobj.email,
            'id': idnormalizer.normalize(fsdobj.email),
            'title': fsdobj.firstName + ' ' + fsdobj.lastName,
            'food_days': days
        }

        try:
            response = requests.post(
                'https://www.75years-im.matem.unam.mx/imregistration',
                headers={'Accept': 'application/json'},
                json=data,
                auth=('user', 'password')
            )
            response.raise_for_status()
        except (ConnectionError, HTTPError) as err:
            api.portal.send_email(
                recipient="gil@im.unam.mx",
                sender="Registro 75",
                subject="Problema en registro",
                body=err,
                immediate=True)
