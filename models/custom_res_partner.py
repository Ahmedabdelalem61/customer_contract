from odoo import models, fields, api


class CustomResPartner(models.Model):
    _inherit = 'res.partner'


    contract_ids = fields.One2many('customer.contract', 'partner_id', string="Contracts", )
    total_confirmed_contracts_price = fields.Float(
        string='Total Confirmed Contracts Price',
        compute='_compute_total_confirmed_contracts'
    )

    @api.depends('contract_ids')
    def _compute_total_confirmed_contracts(self):
        for partner_record in self:
            # partner_record.total_confirmed_contracts_price = sum(
            #     [contract.price for contract in partner_record.contract_ids if contract.state == 'confirmed']
            # )
            # or

            confirmed_contracts = partner_record.contract_ids.filtered(lambda x: x.state == 'confirmed')
            partner_record.total_confirmed_contracts_price = sum(confirmed_contracts.mapped('price'))
