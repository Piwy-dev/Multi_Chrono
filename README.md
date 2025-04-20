# Multi Chrono

Multi Chrono est une application permettant de gérer plusieurs chronomètres ou minuteurs simultatnément.

## Fonctionnalités

- Ajouter et gérer plusieurs chronomètres.
- Démarrer, arrêter et réinitialiser chaque chronomètre individuellement.
- Interface utilisateur simple et intuitive.
- Sauvegarde des chronomètres en cours.

## Installation

1. Clonez ce dépôt :
    ```bash
    HTTP : git clone https://github.com/Piwy-dev/Multi_Chrono.git
    SSH : git clone git@github.com:Piwy-dev/Multi_Chrono.git
    ```
2. Créer un environnement virtuel :
    ```bash
    python -m venv .venv
    ```
3. Activez l'environnement virtuel :
    - Sur Windows :
        ```bash
        .venv\Scripts\activate
        ```
    - Sur macOS et Linux :
        ```bash
        source .venv/bin/activate
        ```
4. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

5. Lancez l'application :
    ```bash
    flask --app=chrono run
    ```

6. Ouvrez votre navigateur et accédez à `http://127.0.0.1:5000`.

## Contribution

Les contributions sont les bienvenues ! 

## Licence

Ce projet est sous licence [GNU v3](LICENSE).

