Feature: Transfer Money and Add Beneficiary
  As a banking user
  I want to manage beneficiaries and transfer funds securely

  Background:
    Given the user is logged in
    And the user is on the dashboard page

  Scenario: Add a new beneficiary with valid details
    When the user navigates to the Add Beneficiary page
    And the user enters account number "123456789012"
    And the user enters IFSC code "ABCD0123456"
    And the user clicks the "Add Beneficiary" button
    Then a success message "Beneficiary added successfully" is displayed

  Scenario: Transfer money to an existing beneficiary within limit
    Given a beneficiary "John Doe" exists
    When the user selects beneficiary "John Doe"
    And the user enters transfer amount "5000"
    And the user proceeds to OTP verification
    And the user enters valid OTP "123456"
    Then the transfer is completed and a confirmation message is shown

  Scenario: OTP verification fails after maximum attempts
    Given a beneficiary "John Doe" exists
    When the user initiates a transfer of amount "5000"
    And the user enters an invalid OTP "000000" five times
    Then the system locks the transaction and displays "Maximum OTP attempts exceeded"

  Scenario Outline: Transfer amount validation
    When the user selects beneficiary "John Doe"
    And the user enters transfer amount "<amount>"
    And the user proceeds to OTP verification
    And the user enters valid OTP "123456"
    Then the system response should be "<expected>"

    Examples:
      | amount   | expected                                 |
      | 5000     | Transfer successful                      |
      | 200000   | Transfer amount exceeds daily limit error |
      | 100000   | Transfer successful (edge of limit)      
