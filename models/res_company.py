# -*- coding: utf-8 -*-

from odoo import models,fields,api,_
from odoo.exceptions import UserError


class Company(models.Model):
    _inherit = "res.company"

    document_seal_ids = fields.One2many('res.company.document.seal','company_id',string='Documents Seals')


    def _get_seal(self,document):
        self.ensure_one()
        try:
            return self.document_seal_ids.filtered(lambda seal_line:seal_line.model_id.model == document).mapped("document_seal")[0]
        except IndexError:
            return False



class DocumentSeal(models.Model):
    _name = 'res.company.document.seal'

    company_id = fields.Many2one("res.company",required=True,ondelete='cascade')
    model_id = fields.Many2one('ir.model',string='Document',domain=[('transient','=',False)],required=True,ondelete='cascade')
    document_seal = fields.Image('Document Seal', copy=False, attachment=True,
                                      max_width=1024, max_height=1024)


