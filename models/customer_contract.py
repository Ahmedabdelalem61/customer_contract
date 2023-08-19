from odoo import models, fields, api
from odoo.exceptions import ValidationError


class CustomerContract(models.Model):
    _name = 'customer.contract'
    _description = "This Model is for Customer Contract"

    STATUS_SELECTION = [('draft', 'Draft'), ('confirmed', 'Confirmed'), ('ended', 'Ended'), ('canceled', 'Canceled')]

    partner_id = fields.Many2one('res.partner', string='Customer', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)

    # set price then make avg price depending on the start and end date days using this (price / days)
    price = fields.Float(string='Price', required=True)
    avg_price = fields.Float(string='Avg Price', compute='_compute_avg_price', store=True)

    # status selection field that has draft, confirmed, ended, and canceled and
    # there are another field that has the last_change_status_by from is auto set to last user that change the status
    state = fields.Selection(STATUS_SELECTION, string='Status', default='draft')
    last_change_state_by_id = fields.Many2one('res.users', string='Last Change Status By')

    @api.onchange('state')
    def _onchange_state(self):
        """
        Update the last_change_state_by field with the current user when state changes.
        """
        self.last_change_state_by_id = self.env.user

    @api.onchange('start_date')
    def _onchange_start_date(self):
        self.end_date = False

    @api.depends('start_date', 'end_date', 'price')
    def _compute_avg_price(self):
        """
        Compute the avg price depending on the start and end date days using this (price / days).
        """
        for rec in self:
            if rec.start_date and rec.end_date and rec.price and rec.start_date <= rec.end_date:
                days = (rec.end_date - rec.start_date).days + 1
                rec.avg_price = rec.price / days
            else:
                rec.avg_price = 0.0

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        """
        Check that the start_date is before the end_date.
        """
        for rec in self:
            if rec.start_date and rec.end_date and rec.start_date > rec.end_date:
                raise ValidationError("The start date must be before the end date.")

