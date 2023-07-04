<!-- ---
title: "Remote Research Intern"
description: "Technical University of Munich (Germany)"
dateString: Aug 2020 - Oct 2020
draft: false
tags: []
showToc: false
weight: 310
--- 
### 🔗 [GitHub](https://github.com/arkalim/pytorch-CycleGAN-and-pix2pix/tree/3D_Seg)

## Description
**Guide:** **Mohammad Farid Azampour** (Visiting Researcher at Chair for Computer Aided Medical Procedures, TU Munich)

<<<<<<< HEAD
My work focused on using **Pix2Pix** (a **CGAN** architecture) to generate **Ultrasound (US) scans** from **MRI scans**, an **image-to-image translation** problem. However, a major challenge that I faced was the lack of structural correspondence between the MRI and US scans, arising from the sheer nature of the way this data is collected. Consequently, I wrote a custom loss function incorporating the **CGAN loss** with a **Dice Loss** between the segmentation maps obtained from the MRI scans and those from the generated US scan. This forces the generator to remove the structural deformation in the generated US scans. Additionally, I was given remote access to the TU-Munich’s cluster computers for training the model as well as an account in their Discourse forum. -->
=======
- Rearchitected Pix2Pix, a CGAN architecture, to generate Ultrasound (US) scans from MRI scans
- Addressed the challenge of structural dissimilarity between MRI and US scans due to data collection methods
- Developed a custom loss function combining CGAN loss and Dice Loss for improved image segmentation
- Implemented the loss function to encourage the generator to eliminate structural deformation in the generated US scans
- Leveraged remote access to TU-Munich's cluster computers for fast model training
- Utilized TU-Munich's Discourse forum for collaboration which drove the project to fruition
>>>>>>> 977ecdc34e75ffdff0de9e2f818e3c13495b8c40
