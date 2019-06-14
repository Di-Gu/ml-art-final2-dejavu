# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 14:14:43 2019

@author: GLH
"""

import os

results_dir = 'results/'
splits = os.listdir(results_dir)

for sp in splits:
    img_fold = os.path.join(results_dir, sp,'images/')
    img_list = os.listdir(img_fold)
    img_real_A = []
    img_real_B = []
    img_fake_B = []
    
    for name in img_list:
        if 'real_A' in name: 
            img_real_A.append(name)
        elif 'real_B' in name: 
            img_real_B.append(name)
        elif 'fake_B' in name: 
            img_fake_B.append(name)
    
    assert len(img_real_A) == len(img_real_B) == len(img_fake_B) , ('xxx')   
      
    num_imgs = len(img_real_A)
       
    full_text = '<p align="center"> real_A &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; real_B &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;| &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;fake_B </p>'    
        
    for i in range(num_imgs):
        full_text += '<p>'+img_real_A[i][:-11]+'</p>'
        full_text += '<p align="center">'
        full_text += '<img src="images/'+img_real_A[i]+'" width="250" title="real_A">'
        full_text += '<img src="images/'+img_real_B[i]+'" width="250" title="real_B">'
        full_text += '<img src="images/'+img_fake_B[i]+'" width="250" title="fake_B">'
        full_text += '</p>'
    
    md_dir = os.path.join(results_dir, sp,'view_results.md')
    with open(md_dir, 'w') as out_file:
        out_file.write(full_text)