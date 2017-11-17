from odoo import api, models, fields

class ResUsersLanguages(models.Model):
    
    _inherit = 'res.users'

    users_lang = fields.Many2many('res.lang', string='Related languages', help='Langs related of the user')
    
    
class IrTranslationExtention(models.Model):

    _inherit = 'ir.translation'
    
    show_hide_lang = fields.Boolean(string='User langs', 
                                    compute='_compute_lang_of_user', 
                                    search='_search_lang_of_user')
        
    @api.depends('lang')
    def _compute_lang_of_user(self):
        user = self.env['res.users'].browse(self.env.uid)
        users_lang_code = [(lang.code) for lang in user.users_lang]
        for record in self:
            if record.lang in users_lang_code:
                record.show_hide_lang = True
            else:
                record.show_hide_lang = False
                
    def _search_lang_of_user(self, operator, value):
        user = self.env['res.users'].browse(self.env.uid)
        operator = 'in'
        value = [(lang.code) for lang in user.users_lang]
        return [('lang', operator, value)]
    
    
class ProductUsersLanguages(models.Model):
    _inherit = 'product.template'
    
    def action_view_user_language_lines(self):
        self.ensure_one()
        action = self.env.ref('base.action_translation').read()[0]
        action['domain'] = [('res_id', '=', self.id)]
        action['context'] = {
                'search_default_showhidelang': True,
            }
        return action
    
    
    
    
    