Feature: Instant Fund Transfer
  As a registered user
  I want to manage beneficiaries and perform fund transfers
  So that I can send money securely and efficiently

  Background:
    Given the user is logged in
    And the user has at least one beneficiary

  Scenario: Verify adding a beneficiary with valid details
    When the user navigates to the Beneficiary Management screen
    And the user clicks on "Add Beneficiary"
    And the user enters a valid account number, IFSC code and name
    And the user saves the beneficiary
    Then a success toast is displayed
    And the new beneficiary appears in the list

  Scenario: Verify successful money transfer to an existing beneficiary
    When the user opens the Transfer screen
    And the user selects an existing beneficiary
    And the user enters a valid amount within limits
    And the user proceeds and enters the correct OTP
    Then the transfer is completed
    And a confirmation message is shown
    And the transaction appears in history

  Scenario: Verify OTP verification flow works for a transfer
    When the user initiates a transfer with a valid amount
    And the user requests OTP
    And the user enters the correct OTP received on mobile
    Then the transfer succeeds
    And a success notification is displayed

  Scenario Outline: Verify transfer amount validation
    When the user attempts to transfer <amount>
    Then the system should display <message>

    Examples:
      | amount | message                                          |
      | 150000| Transfer amount exceeds limit of ₹1,00,000       |
      | 1     | Transfer of ₹1 is processed successfully       |
      | 0     | Transfer amount must be greater than zero        |
