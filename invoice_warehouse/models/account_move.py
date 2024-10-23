from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = 'account.move'

    user_warehouse_id = fields.Many2one(
        'stock.warehouse',
        string="Warehouse",
        compute="_compute_user_warehouse",
        store=False
    )

    @api.depends('create_uid')
    def _compute_user_warehouse(self):
        for record in self:
            if record.create_uid and record.create_uid.property_warehouse_id:
                record.user_warehouse_id = record.create_uid.property_warehouse_id
            else:
                record.user_warehouse_id = False
