from odoo import api, fields, models

class WebPortal(models.Model):
    _name = 'web.portal'
    _description = 'Web Portal'
    
    name = fields.Char('name')
    address = fields.Char('url address', required=True)
    login = fields.Char('login', required=True)
    password = fields.Char('password', required=True)
    partner = fields.Char('partner', required=True)
    status = fields.Selection([('draft', 'Draft'), ('deployed', 'Deployed'), 
        ('closed','Closed'), ('error', 'Error'), ('ready', 'Ready')], 'Status',default='draft')
    
    @api.one
    def do_check_portal(self):
        import requests
        #url = 'http://0.0.0.0:8069'
        try:
            res = requests.head(self.address)
            if res.status_code == 200:
                self.status = 'deployed'
            if res.status_code != 200:
                self.status = 'error'
        except :
            self.status = 'closed'
        
        return True
    
    @api.model
    def do_check_portall_all(self):
        import requests
        
        portals = self.search([('status', '<>', 'draft')])
        
        for url in portals:
            try:
                res = requests.head(url.address)
                if res.status_code == 200:
                    url.status = 'deployed'
                if res.status_code != 200:
                    url.status = 'error'
            except :
                url.status = 'closed'
        
        return True
    