Feature: Test du service web

  Scenario: Vérification de la réponse de l'API
    Given J'ai accès au service web à l'URL "https://jsonplaceholder.typicode.com"
    When Je fais une requête GET à l'operation "/todos/1"
    Then La réponse HTTP doit avoir le code de statut 200
    And Le contenu de la réponse doit contenir "delectus"

