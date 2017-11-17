import json
from odoo import api, models, fields

json_path = 'C:\\odoo\\dimgunner\\performance\\odoo-10.0\\custom-addons\\mo_medication_product\\json\\'
json_product_template = json_path + 'medic_product_templates.json'
json_product_template_divided_info = json_path + 'medic_product_templates_divided_info.json'


class MedicationProductTemplate(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'

    import_id = fields.Text('Import ID', readonly=True)

    info_general = fields.Text('General information',translate=True)
    info_directions = fields.Text('Directions', translate=True)
    info_precautions = fields.Text('Precautions', translate=True)
    info_contraindications = fields.Text('Contraindications', translate=True)
    info_side_effect = fields.Text('Possible side effect', translate=True)
    info_drug_interactions = fields.Text('Drug interactions', translate=True)
    info_missed_dose = fields.Text('Missed dose', translate=True)
    info_overdose = fields.Text('Overdose', translate=True)
    info_storage = fields.Text('Storage', translate=True)
    info_note = fields.Text('Note', translate=True)
    info = fields.Text('Product Info', translate=True)

    def _cron_divide_products_info(self):
        with open(json_product_template, 'r') as fp:
            products = json.load(fp)

        # products = products[:2]

        for idx, product in enumerate(products):

            if product['import_id'] == 91:
                pass

            for i, tab in enumerate(product['product_info']['product_info_tabs']):

                title = tab['title'].strip()

                if title == 'General information':
                    product['info_general'] = tab['section']

                if title == 'Directions':
                    product['info_directions'] = tab['section']

                if title == 'Precautions':
                    product['info_precautions'] = tab['section']

                if title == 'Contraindications':
                    product['info_contraindications'] = tab['section']

                if title == 'Possible side effect':
                    product['info_side_effect'] = tab['section']

                if title == 'Drug interactions':
                    product['info_drug_interactions'] = tab['section']

                if title == 'Missed dose':
                    product['info_missed_dose'] = tab['section']

                if title == 'Overdose':
                    product['info_overdose'] = tab['section']

                if title == 'Storage':
                    product['info_storage'] = tab['section']

                if title == 'Note':
                    product['info_note'] = tab['section']

            del product['product_info']
            del product['info']

        with open(json_product_template_divided_info, 'w') as fp:
            json.dump(products, fp)

    @api.multi
    def _cron_import_products(self):
        with open(json_product_template_divided_info, 'r') as fp:
            import_products = json.load(fp)

        product_template = self.env['product.template']

        # rs = self.env['product.template'].search([])

        for product in import_products:
            d = {
                'import_id': str(product['import_id']),
                'name': product['name'],
                'description': product['description'],
                'image': product['image'],

                # 'info': product['info'],

                'info_general': product.get('info_general', ''),
                'info_directions': product.get('info_directions', ''),
                'info_precautions': product.get('info_precautions', ''),
                'info_contraindications': product.get('info_contraindications', ''),
                'info_side_effect': product.get('info_side_effect', ''),
                'info_drug_interactions': product.get('info_drug_interactions', ''),
                'info_missed_dose': product.get('info_missed_dose', ''),
                'info_overdose': product.get('info_overdose', ''),
                'info_storage': product.get('info_storage', ''),
                'info_note': product.get('info_note', ''),

                # 'info': product['info'],
            }

            rs = product_template.search([('import_id', '=', str(product['import_id']))], limit=1)

            if rs:
                rs.update(d)
            else:
                product_template.create(d)

        pass
    
    def _cron_import_translate(self):
        
        lang = {
            'fr':'fr_FR', 
            'en':'en_US', 
            'de':'de_DE', 
            'it':'it_IT', 
            'ar':'ar_SY', 
            'es':'es_ES', 
            'ru':'ru_RU', 
            'ua':'uk_UA'
        }
        
        product_template = self.env['product.template']
        product_translate = self.env['ir.translation']
        lang_active = self.env['res.lang']
        
        def make_record(product_translate, name, id, lg, value):
            
            d = {
                'name': name,
                'res_id': id,
                'lang': lg,
                'type': 'model',
                'value': value,
                'module': '__export__',
                'state': 'translated',
            }
                
            rs_tr = product_translate.search([ 
                ('res_id', '=', id), 
                ('lang', '=', lg),
                ('name', '=', name) 
            ], limit=1)
                                    
            if rs_tr:
                rs_tr.update(d)
            else:
                product_translate.create(d)
                
            #data_ex.env.cr.commit()
        
        #json_info =  '../my_json/medic_processed_products_all.json'
        #json_info =  '../my_json/test_abana.json'
        #json_info = '/home/igor/Downloads/test_abana.json'
        json_info = '/home/igor/Downloads/medic_processed_products_all.json'
        
        with open(json_info) as data_file:
            data = json.load(data_file) 
            
            rounds = data['product_lang']
            
            for row in rounds: 
                for key in row.keys():
                    if key != 'id':
                        lg = lang.get(key,'')
                        if lg: 
                            lg_act = lang_active.search([('code', '=', lg)], limit=1)
                            if lg_act:
                                if lg_act.active:
                                    rs_pt = product_template.search([('import_id', '=', str(row[key]['product_id']))], limit=1)
                                    if rs_pt:
                                
                                        #head
                                        name = "%s,%s" % ('product.template', 'name')
                                        make_record(product_translate, name, rs_pt.id, lg, row[key]['product_head'])
                                        #product_text
                                        name = "%s,%s" % ('product.template', 'description_sale')
                                        make_record(product_translate, name, rs_pt.id, lg, row[key]['product_text'])
                                        
                                        print(lg, row[key]['product_id'])
                                        
                                        lenItems = len(row[key]['product_info']['product_info_tabs'])
                                        
                                        if lenItems >= 1:
                                            #product_info
                                            name = "%s,%s" % ('product.template', 'info_general')
                                            make_record(product_translate, name, rs_pt.id, lg, row[key]['product_info']['product_info_tabs'][0]['section'])
                                        if lenItems >= 2:
                                            name = "%s,%s" % ('product.template', 'info_directions')
                                            make_record(product_translate, name, rs_pt.id, lg, row[key]['product_info']['product_info_tabs'][1]['section'])
                                        if lenItems >= 3:
                                            name = "%s,%s" % ('product.template', 'info_precautions')
                                            make_record(product_translate, name, rs_pt.id, lg, row[key]['product_info']['product_info_tabs'][2]['section'])
                                        if lenItems >= 4:
                                            name = "%s,%s" % ('product.template', 'info_contraindications')
                                            make_record(product_translate, name, rs_pt.id, lg, row[key]['product_info']['product_info_tabs'][3]['section'])
                                        if lenItems >= 5:
                                            name = "%s,%s" % ('product.template', 'info_side_effect')
                                            make_record(product_translate, name, rs_pt.id, lg, row[key]['product_info']['product_info_tabs'][4]['section'])
                                        if lenItems >= 6:
                                            name = "%s,%s" % ('product.template', 'info_drug_interactions')
                                            make_record(product_translate, name, rs_pt.id, lg, row[key]['product_info']['product_info_tabs'][5]['section'])
                                        if lenItems >= 7:
                                            name = "%s,%s" % ('product.template', 'info_missed_dose')
                                            make_record(product_translate, name, rs_pt.id, lg, row[key]['product_info']['product_info_tabs'][6]['section'])
                                        if lenItems >= 8:
                                            name = "%s,%s" % ('product.template', 'info_overdose')
                                            make_record(product_translate, name, rs_pt.id, lg, row[key]['product_info']['product_info_tabs'][7]['section'])
                                        if lenItems >= 9:
                                            name = "%s,%s" % ('product.template', 'info_storage')
                                            make_record(product_translate, name, rs_pt.id, lg, row[key]['product_info']['product_info_tabs'][8]['section'])
                                        if lenItems >= 10:
                                            name = "%s,%s" % ('product.template', 'info_note')
                                            make_record(product_translate, name, rs_pt.id, lg, row[key]['product_info']['product_info_tabs'][9]['section'])
                                    
        pass
                                
