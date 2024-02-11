gene_synonyms = {
        'RYR1' : ['RYR1'],
        'KCNH2' : ['KCNH2'],
        'LMNA' : ['LMNA'],
        'KCNQ1' : ['KCNQ1'],
        'high tumor mutational burden' : ['genes','gene'],
        'extensive tumor infiltrating lymphocytes' : ['genes','gene'],
        'no tumor infiltrating lymphocytes' : ['genes','gene'],
        'LDH' : ['LDH'],
        'APC' : ['APC'],
        'PD-L1': ['PD-L1'],
        'NF1': ['NF1'],
        'SCN5A': ['SCN5A'],  # TODO
        'PCSK9': ['PCSK9'],  # TODO
        'TGFBR2': ['TGFBR2'],  # TODO
        'ACTA2': ['ACTA2'],  # TODO
        'PIK3R1': ['PIK3R1'],  # TODO
        'BRCA1': ['BRCA1'],  # TODO
        'AURKA': ['AURKA'],  # TODO
        'SND1': ['SND1'],  # TODO
        'MLH1': ['MLH1'],  # TODO
        'ROS1': ['ROS1'],  # TODO
        'EZR': ['EZR'],  # TODO
        'RANBP2': ['RANBP2'],  # TODO
        'PDGFRA': ['PDGFRA', 'PDGFR2', 'PDGF-R', 'CD140'],
        'FGFR3': ['FGFR3', 'JTK4', 'CD333', 'CEK2', 'FGFR-3', 'ACH', 'HSFGFR3EX'],
        'ATM': ['ATM', 'TELO', 'TEL1', 'ATDC', 'ATA', 'ATC', 'ATD'],
        'FLT3': ['FLT3', 'STK1', 'FLK2', 'CD135'],
        'high tumor mutational burden': ['gene', 'mutations'],
        'extensive tumor infiltrating lymphocytes': ['infiltrating lymphocytes'],
        'no tumor infiltrating lymphocytes': ['no infiltrating lymphocytes'],
        'PTCH1': ['PTCH1', 'PTCH', 'BCNS', 'PTC', 'PTC1'],
        'MDM2': ['MDM2', 'MGC5370', 'HDM2'],
        'ABL1': ['ABL', 'ABL1', 'JTK7', 'P150', 'C-ABL', 'BCR/ABL', 'BCR-ABL'],
        'ROS1': ['ROS', 'ROS1', 'C-Ros-1', 'MCF3'],
        'CDK4': ['CDK4', 'CDK_4', 'CDK4/6', 'CMM3', 'PSK-J6', 'CDK2/4/6', 'CDK'],
        'CDK6': ['CDK6', 'CDK4/6', 'PLSTIRE', 'MCPH12', 'CDK2/4/6', 'CDK'],
        'KRAS': ['KRAS', 'C-K-RAS', 'CFC2', 'K-RAS2A', 'K-RAS2B', 'K-RAS4A', 'K-RAS4B', 'K-Ras',  'KI-RAS', 'KRAS1', 'KRAS2', 'NS', 'NS3', 'RALD', 'RASK2', 'c-Ki-ras', 'c-Ki-ras2'],
        'BRAF': ['BRAF', 'B-RAF1', 'B-raf', 'BRAF-1', 'BRAF1', 'NS7', 'RAFB1'],
        'NF2': ['NF2', 'ACN', 'BANF', 'SCH', 'merlin-1'],
        'AKT1': ['AKT1', 'AKT', 'PKB', 'PKB-ALPHA', 'PRKBA', 'RAC', 'RAC-ALPHA'],
        'CDKN2A': ['CDKN2A', 'ARF', 'CDK4I', 'CDKN2', 'CMM2', 'INK4', 'INK4A', 'MLM', 'MTS-1', 'MTS1', 'P14', 'P14ARF', 'P16', 'P16-INK4A', 'P16INK4', 'P16INK4A', 'P19', 'P19ARF', 'TP16', 'p53/p16-Independent'],
        'NRAS': ['NRAS', 'ALPS4', 'CMNS', 'KRAS', 'N-ras', 'NCMS', 'NRAS1', 'NS6'],
        'EGFR': ['EGFR', 'ERBB', 'ERBB1', 'ERRP', 'HER1', 'NISBD2', 'PIG61', 'mENA'],
        'EML4': ['EML4', 'C2orf2', 'ELP120', 'EMAP-4', 'EMAPL4', 'ROPP120'],
        'KIT': ['KIT', 'C-Kit', 'CD117', 'MASTC', 'PBT', 'SCFR'],
        'PIK3CA': ['PIK3CA', 'CCM4', 'CLAPO', 'CLOVE', 'CWS5', 'MCAP', 'MCM', 'MCMTC', 'PI3K', 'PI3K-alpha', 'p110-alpha'],
        'BRCA2': ['BRCA2', 'BRCC2', 'BROVCA2', 'FACD', 'FAD', 'FAD1', 'FANCD', 'FANCD1', 'GLM3', 'PNCA2', 'XRCC11'],
        'IDH1': ['IDH1', 'HEL-216', 'HEL-S-26', 'IDCD', 'IDH', 'IDP', 'IDPC', 'PICD'],
        'STK11': ['STK11', 'LKB1', 'PJS', 'hLKB1'],
        'PTEN': ['PTEN', '10q23del', 'BZS', 'CWS1', 'DEC', 'GLM2', 'MHAM', 'MMAC1', 'PTEN1', 'PTENbeta', 'TEP1'],
        'CDK6': ['CDK6', 'CDK_6', 'CDK4/6', 'CDK_4/6', 'MCPH12', 'PLSTIRE'],
        'FGFR1': ['FGFR1', 'BFGFR', 'CD331', 'CEK', 'ECCL', 'FGFBR', 'FGFR-1', 'FLG', 'FLT-2', 'FLT2', 'HBGFR', 'HH2', 'HRTFDS', 'KAL2', 'N-SAM', 'OGD', 'bFGF-R-1'],
        'MDM2': ['MDM2', 'ACTFS', 'HDMX', 'LSKB', 'hdm2'],
        'ALK': ['ALK', 'ALK1', 'CD246', 'NBLST3'],
        'ERBB2': ['ERBB2', 'CD340', 'HER-2', 'HER-2/neu', 'HER2', 'MLN_19', 'NEU', 'NGL', 'TKR1', 'VSCN2', 'c-ERB-2', 'c-ERB2'],
        'MET': ['MET', 'AUTS9', 'DFNB97', 'HGFR', 'RCCP2', 'c-Met'],
        'TP53': ['TP53', 'BCC7', 'BMFS5', 'LFS1', 'P53', 'TRP53'],
        'ERBB3': ['ERBB3', 'ErbB-3', 'FERLK', 'HER3', 'LCCS2', 'MDA-BF-1', 'VSCN1', 'c-erbB-3', 'c-erbB3', 'erbB3-S', 'p180-ErbB3', 'p45-sErbB3', 'p85-sErbB3'],
        'RB1': ['RB1', 'OSRC', 'PPP1R130', 'RB', 'p105-Rb', 'p110-RB1', 'pRb', 'pp110'],
        'NTRK1': ['MTC', 'TRK', 'TRK1', 'TRKA', 'Trk-A', 'p140-TrkA'],
        'RET': ['RET', 'CDHF12', 'CDHR16', 'PTC', 'RET51'],
        'SMO' : ['SMO']
    }