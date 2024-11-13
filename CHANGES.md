# Tacotron2 Modifications

## Overview

This repository contains modifications to the original Tacotron2 codebase, aiming to improve compatibility with the latest versions of dependencies and enhance workflow automation.

## Changes Made

### 1. **Python Script: `file_list_updater.py`**
A new Python file, `file_list_updater.py`, has been added to update the `.wav` file paths in the dataset file list. The script does the following:

- **Purpose**: It adds a full path prefix to each `.wav` file reference in the dataset file list (e.g., training, validation, and test files).
- **Functionality**: 
    - Reads the original file lists.
    - Updates each line by adding the specified full path prefix to the `.wav` filenames.
    - Saves the modified file list back to the same file.
- **Usage**: You can run the script to automatically update your file paths.

Example of how the file list is updated:
```bash
C:\Users\YOURUSERNAME\tacotron2\filelists\wavs\LJ033-0149.wav|the FBI Laboratory developed a latent palmprint and latent fingerprint on the bag.
```

### 2. **TensorFlow Compatibility: Updated hparams.py**
The original code in hparams.py used the deprecated tf.contrib module, which is no longer available in newer versions of TensorFlow. To resolve this issue:

**Changes Made**:
- Removed all instances of tf.contrib.
- Replaced the tf.contrib.training.HParams with a custom class to manage hyperparameters.
- Benefit: Ensures compatibility with the latest version of TensorFlow and prevents errors related to deprecated code.
