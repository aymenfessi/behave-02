Feature: Test du service web avec objet

  Scenario: Utiliser une table de données pour passer un objet
    Given J'ai accès au service web à l'URL "https://jsonplaceholder.typicode.com"
    When Je fais une requête GET à l'operation "/todos/1"
    Then La réponse HTTP doit avoir le code de statut 200
    And Le contenu de la réponse doit être égal à cet objet
      | user_id | id | title                | completed |
      | 1       | 1  | delectus aut autem   | false     |