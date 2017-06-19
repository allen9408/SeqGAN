import numpy as np
from enum import Enum
class Activity(Enum):
	start = 0
	bair_hugger_preparation_ec = 1
	yankauer_suction_preparation_ro = 2
	oxygen_preparation_bc = 3
	pt_arrival = 4
	pre_cnmc_tasks = 5
	ems_c_collar_cs = 6
	visual_assessment_aa = 7
	verbal_assessment_aa = 8
	passive_oxygen_applied_bc = 9
	oxygen_bc = 10
	oxygen_held_bc = 11
	chest_auscultation_ba = 12
	r_dp_pt_pc = 13
	pulse_ox_placement_ba = 14
	l_dp_pt_pc = 15
	oxygen_removed_bc = 16
	pulse_oximetry_os = 17
	cardiac_lead_placement_ca = 18
	r_brachial_radial_pc = 19
	l_brachial_radial_pc = 20
	verbal_assessed_gcs = 21
	eyes_assessed_gcs = 22
	clothing_removed_ec = 23
	eyes_verbalized_gcs = 24
	verbal_verbalized_gcs = 25
	motor_assessed_gcs = 26
	warm_sheet_placement_ec = 27
	total_verbalized_gcs = 28
	abp_cuff_placement_ca = 29
	right_pupil_pu = 30
	left_pupil_pu = 31
	mbp_bp = 32
	temperature_ea = 33
	abp_bp = 34
	palpation_h = 35
	palpation_f = 36
	palpation_n = 37
	light_inspection_n = 38
	r_otoscopy_ear = 39
	l_otoscopy_ear = 40
	palpation_ne = 41
	palpation_c = 42
	palpation_a = 43
	stability_pe = 44
	palpation_rle = 45
	joints_ranged_rle = 46
	iv_placement_confirmation_cc = 47
	visual_inspection_lle = 48
	palpation_lle = 49
	blood_drawn_sa = 50
	joints_ranged_lle = 51
	ems_c_collar_removal_cs = 52
	miami_j_collar_application_cs = 53
	miami_j_collar_cs = 54
	log_roll_bk = 55
	c_spine_bk = 56
	t_spine_bk = 57
	l_spine_bk = 58
	rectal_bk = 59
	pain_medication_sa = 60
	bair_hugger_ec = 61
	cxr_sa = 62
	pt_departure = 63
	warm_sheet_preparation_ec = 64
	manual_in_line_cs = 65
	motor_verbalized_gcs = 66
	light_inspection_m = 67
	iv_placement_cc = 68
	palpation_rue = 69
	manual_inspection_g = 70
	palpation_lue = 71
	joints_ranged_lue = 72
	joints_ranged_rue = 73
	c_spine_clearance_sa = 74
	doppler_exam_sa = 75
	palpation_m = 76
	capillary_refill_cr = 77
	iv_bolus_connected_b = 78
	iv_bolus_given_b = 79
	iv_bolus_disconnected_b = 80
	iv_placement_2_cc = 81
	miami_j_collar_adjustment_cs = 82
	r_femoral_pc = 83
	l_femoral_pc = 84
	chest_visual_ba = 85
	suction_oropharynx_ro = 86
	bandage_placed_sa = 87
	bag_ventilation_i = 88
	r_pupil_ey = 89
	l_pupil_ey = 90
	miami_j_collar_removal_cs = 91
	non_warm_sheet_placement_ec = 92
	palpation_non_spine_bk = 93
	warm_sheet_ec = 94
	warm_sheet_intentionally_removed_ec = 95
	iv_confirmation_cc = 96
	non_warm_sheet_ec = 97
	paplation_c = 98
	non_warm_sheet_intentionally_removed_ec = 99
	end = 100

# print(Activity(64).name)
f = open('save/generator_sample.txt')
i = open('save/real_sequence.txt')
o = open('save/sequence.txt', 'w+')
o1 = open('save/sequenceIndex.txt', 'w+')
o2 = open('save/realSequenceIndex.txt', 'w+')
line = i.readline()
while line:
	vector = line.split()
	for index in vector:
		if int(index) > 0 and int(index) < 100:
			o2.write(index)
			o2.write(' -1 ')
	o2.write('-2\n')
	line = i.readline()
i.close()
o2.close()

line = f.readline()
while line:
	vector = line.split()
	for index in vector:
		if int(index) > 0 and int(index) < 100:
			o.write(Activity(int(index)).name)
			o.write(',')
			o1.write(index)
			o1.write(' -1 ')

	o.write('\n')
	o1.write('-2\n')
	line = f.readline()

f.close()
o.close()
o1.close()