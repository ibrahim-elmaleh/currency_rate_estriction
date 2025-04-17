# from odoo import models, fields, api
# from odoo.exceptions import ValidationError
#
# class ResCurrency(models.Model):
#     _inherit = 'res.currency'
#
#     @api.constrains('rate_ids')
#     def _check_only_one_rate_line(self):
#         for currency in self:
#             if currency.active and len(currency.rate_ids) > 1:
#                 raise ValidationError("لا يمكن إضافة أكثر من سطر واحد في أسعار العملة.")

from odoo import models, api
from odoo.exceptions import ValidationError

class ResCurrency(models.Model):
    _inherit = 'res.currency'

    @api.constrains('rate_ids')
    def _check_only_one_rate_line(self):
        for currency in self.filtered(lambda c: c.rate_ids):
            if len(currency.rate_ids) > 1:
                raise ValidationError("لا يمكن إضافة أكثر من سطر واحد في أسعار العملة.")
