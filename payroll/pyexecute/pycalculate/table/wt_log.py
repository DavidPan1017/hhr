# -*- coding: utf-8 -*-

from ....pysysutils import global_variables as gv
from .....utils import get_current_dttm


class WTLog:
    """
    Desc: 薪资计算薪资项目过程日志 HHR_PY_WT_LOG
    Author: David
    Date: 2018/11/29
    """

    __slots__ = [
        'db',
        'run_parm',
        'tenant_id',
        'emp_id',
        'emp_rcd',
        'seq_num',
        'tree_node_num',
        'cal_id',
        'cur_cal_id',
        'in_out_flag',
        'seg'
    ]

    def __init__(self, **kwargs):
        self.db = gv.get_db()
        self.run_parm = gv.get_run_var_value('RUN_PARM')
        self.tenant_id = kwargs.get('tenant_id', 0)
        self.emp_id = kwargs.get('emp_id', '')
        self.emp_rcd = kwargs.get('emp_rcd', 1)
        self.seq_num = kwargs.get('seq_num', 0)
        self.tree_node_num = kwargs.get('tree_node_num', 0)
        self.cal_id = kwargs.get('cal_id', '')
        self.cur_cal_id = kwargs.get('cur_cal_id', '')
        self.in_out_flag = kwargs.get('in_out_flag', '')
        self.seg = kwargs.get('seg', None)

    def insert(self):
        wt_log = self.db.get_table('hhr_py_wt_log', schema_name='boogoo_payroll')
        if self.seg.segment_num == "*":
            self.seg.segment_num = 999
        ins = wt_log.insert()
        val = [
            {'tenant_id': self.tenant_id,
             'hhr_empid': self.emp_id,
             'hhr_emp_rcd': self.emp_rcd,
             'hhr_seq_num': self.seq_num,
             'hhr_tree_node_num': self.tree_node_num,
             'hhr_segment_num': self.seg.segment_num,
             'hhr_py_cal_id': self.cal_id,
             'hhr_f_cal_id': self.cur_cal_id,
             'hhr_bf_af_flag': self.in_out_flag,
             'hhr_pin_cd': self.seg.pin_id,
             'hhr_amt': self.seg.amt,
             'hhr_currency': self.seg.currency,
             'hhr_prcs_flag': self.seg.prcs_flag,
             'hhr_bgn_dt': self.seg.bgn_dt,
             'hhr_end_dt': self.seg.end_dt,
             'hhr_std_amt': self.seg.std_amt,
             'hhr_retro_amt': self.seg.retro_amt,
             'hhr_quantity': self.seg.quantity,
             'hhr_quanty_unit': self.seg.quantity_unit,
             'hhr_ratio': self.seg.ratio,
             'hhr_init_amt': self.seg.init_amt,
             'hhr_init_cur': self.seg.init_currency,
             'hhr_seg_rule_cd': self.seg.seg_rule_id,
             'hhr_round_rule': self.seg.round_rule_id,
             'hhr_formula_id': self.seg.formula_id,
             'hhr_accm_type': self.seg.acc_type,
             'hhr_create_dttm': get_current_dttm(),
             'hhr_create_user': self.run_parm['operator_user_id'],
             'hhr_modify_dttm': get_current_dttm(),
             'hhr_modify_user': self.run_parm['operator_user_id'],
             }]
        self.db.conn.execute(ins, val)
