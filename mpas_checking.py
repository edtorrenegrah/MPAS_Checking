from openerp.osv import fields, osv


class mpas_checking(osv.osv):
    _name = "mpas.checking"
    _description = "Accounting Checking Request Log"

    _columns = {
        't_type': fields.selection([
            ('empoyee_name', 'Employee Name'),
            ('temp_transaction', 'Temporary Transaction'),
        ], 'Type', required=True),
        'c_id': fields.char('Transaction ID', size=128, required=True),
        'field1': fields.char('Employee Name', size=128, required=True),
        'date': fields.date('Date', required=True),
        'amount': fields.float('Amount'),
    }
