Feature: Add Beneficiary and Instant Transfer
  As a banking user I want to manage beneficiaries and transfer funds instantly

  Background:
    Given the user is logged in
    And the user has a valid authentication token

  Scenario: Add a beneficiary with valid details
    When the user navigates to the Add Beneficiary page
    And the user enters account number "123456789012"
    And the user enters IFSC code "QRST0001234"
    And the user clicks the "Add Beneficiary" button
    Then a success confirmation is displayed

  Scenario: Transfer funds within limit to a registered beneficiary
    Given the user has at least one registered beneficiary
    When the user navigates to the Transfer page
    And the user selects beneficiary "John Doe"
    And the user enters amount "5000"
    And the user clicks "Proceed"
    And the user enters OTP "123456"
    Then the transfer is completed and a confirmation message is shown

  Scenario: OTP verification succeeds for a transfer
    Given the user has initiated a transfer
    When the user receives an OTP "654321"
    And the user enters the OTP "654321"
    Then the transaction is marked successful

  Scenario Outline: Transfer fails after three incorrect OTP attempts
    Given the user has initiated a transfer
    When the user enters OTP "<otp1>" and submits
    Then an error message is shown
    When the user enters OTP "<otp2>" and submits
    Then an error message is shown
    When the user enters OTP "<otp3>" and submits
    Then the transaction is cancelled and a failure message is displayed

    Examples:
      | otp1   | otp2   | otp3   |
      | 111111 | 222222 | 333333 |