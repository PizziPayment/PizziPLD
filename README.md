# PizziPLD
Product Log Document for Pizzi, fueled by Pandoc, Markdown and Latex

# Requirement
You need `Pandoc`, `GNU Make`, `Python3` and `Tectonic` (or any latex compiler) to compile the PLD.

Notice that a `build.nix` can provide you the environment required to compile.

# How to compile PLD ?

```sh
$> make 
```

# How to modify cards ?

A card file is structured like this:

```yaml
title: Back-end  # The actual title of the array
groups:  # The groups of the cards 
  - name: 3.1 - Authentification  # Name of the group, usually starts with a `X.Y` id
    stories:  # All the stories associated to the group
      - name: 3.1.1 - Créer un compte  # Name of the user story, usually starts with a `X.Y.Z` id
        state: finished  # The state of the task associated to the story `unstarted`, `progressing`, `finished`, `delayed`, `abandoned`
```

All the cards are located in `./src/cards/...`.


# How to modify / add user stories ?

A user story file is structured lik this

```yaml
id: 2.1.1  # The id of the user story, same as the one in the card array
title: Inscription  # Name of the user story, same as the one in the card array
as: Commerçant  # The targeted user
iWantTo: M'inscrire  # The desired action
description: Le logiciel commerçant doit permettre au commerçant de s’inscrire de sorte à ce qu’il puisse utiliser toutes les fonctionnalités du logiciel par la suite  # Action description
definitionOfDone:  # A list of definition of done
  - Le logiciel possède une page afin de récupérer l’email et le mot de passe que le commerçant aura entré
  - Le mot de passe doit contenir plus de 8 caractères
  - Le commerçant peut s’inscrire au service
  - En cas de succès un mail de confirmation d’inscription sera envoyé
  - En cas d’erreur, le commerçant sera invité à recommencer l’étape via un message
estimation: 2  # Estimation of work in days
```

All the files are located in `./src/user_stories/<work group>/`

To add a card you have to name following these rules:
`X.Y.Z_english_name.yaml`

If `Y` or `Z` are digits, please add a `0` in front of them to correctly order the cards in the directory and in the pld.

Exemple: `3.01.01_register.yaml`
