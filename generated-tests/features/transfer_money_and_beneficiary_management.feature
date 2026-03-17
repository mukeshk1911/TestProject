Feature: Transfer Money and Beneficiary Management
  Background:
    Given the user is logged into the mobile banking app
    And the user is on the appropriate page for the scenario

  Scenario: Verify adding a beneficiary with valid details
    When the user navigates to the Add Beneficiary page
    And enters a valid account number "123456789012"
    And enters a valid IFSC code "MNOP0123456"
    And enters beneficiary name "John Doe"
    And clicks the "Add Beneficiary" button
    Then a success toast is displayed
    And the new beneficiary appears in the beneficiary list

  Scenario: Verify transferring money within limits with correct OTP
    When the user selects an existing beneficiary
    And enters transfer amount "5000"
    And proceeds to request OTP
    And provides the correct OTP "123456"
    And confirms the transfer
    Then a confirmation message "Transfer successful" is shown

  Scenario: Verify error when adding beneficiary with invalid account number
    When the user navigates to the Add Beneficiary page
    And enters an invalid account number "ABC123"
    And enters a valid IFSC code "ABCD0123456"
    And clicks the "Add Beneficiary" button
    Then a validation error stating "Account number must be numeric and 10‑16 digits" is displayed

  Scenario Outline: Verify transaction history API returns recent transfer
    Given a successful transfer of amount <amount> to beneficiary <beneficiary_id>
    When the user sends a GET request to "/api/transactions?userId=<userId>"
    Then the response contains a transaction with amount <amount>, beneficiary <beneficiary_id>, and status "Success"

    Examples:
      | amount | beneficiary_id | userId |
      | 5000   | BEN123         | USER123 |
