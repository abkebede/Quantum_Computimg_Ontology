# GitHub Upload and Jupyter Notebook Use

## 1. Remove personal computer paths before uploading

A public GitHub repository should not contain instructor-specific paths such as:

```text
C:\Users\yourname\Documents\...
```

Use generic placeholders instead:

```text
<YOUR_PROJECT_FOLDER>\qc-code-study-library
```

This repository has been cleaned to use generic placeholders. Students should replace the placeholders with the folder location on their own computers.

## 2. Upload the unzipped folder contents

Do not upload the ZIP file itself as the project. Unzip the package first, then upload the files and folders into the GitHub repository.

Recommended upload method:

1. Create a new GitHub repository.
2. Unzip `qc-code-study-library.zip` on your computer.
3. Open the unzipped `qc-code-study-library` folder.
4. Select all contents inside the folder.
5. Drag the selected files and folders into GitHub's **Add file → Upload files** page.
6. Commit the uploaded files.

## 3. What GitHub does with `.ipynb` notebooks

GitHub can display Jupyter notebooks in the browser, but the notebook is normally static. That means viewers can see the notebook cells and saved outputs, but the code is not automatically executed just by opening the file on GitHub.

To run notebooks from GitHub, use one of these methods:

- Clone or download the repository and run Jupyter locally.
- Open the repository in GitHub Codespaces and run the notebooks there.
- Open selected notebooks in Google Colab, if the code does not require local credentials.
- Use Binder or another live notebook service, if configured.

## 4. Local Jupyter workflow after downloading from GitHub

On a Windows computer:

```bat
C:\qgss_env\Scripts\activate
cd <YOUR_PROJECT_FOLDER>\qc-code-study-library
jupyter notebook
```

Then open an `.ipynb` notebook or create a new notebook.

Use the kernel:

```text
Python (qgss_env)
```

## 5. GitHub Codespaces workflow

GitHub Codespaces can run the repository in a browser-based development environment. This repository includes a `.devcontainer/devcontainer.json` file to help Codespaces install the needed Python packages.

Suggested workflow:

1. Open the repository on GitHub.
2. Click **Code**.
3. Choose **Codespaces**.
4. Create a new codespace.
5. Open a notebook file.
6. Select the Python environment provided by the codespace.
7. Run the notebook cells.

Do not paste an IBM Quantum API key into a public codespace notebook that will be committed back to GitHub. Use private secrets or run hardware-access notebooks locally.

## 6. Hardware notebooks and API keys

Files in `05_ibm_hardware/` are templates. They should not contain a real API key.

Safe placeholder:

```text
PASTE_YOUR_API_KEY_HERE
```

Never commit:

```text
real IBM Quantum API key
screenshots showing API keys
private token files
secrets.json
.env
```

