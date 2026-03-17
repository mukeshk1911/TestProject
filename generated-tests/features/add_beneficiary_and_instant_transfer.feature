Feature: Add Beneficiary and Instant Transfer
  Background:
    Given user is logged in

  Scenario: Add beneficiary with valid details
    Given user navigates to Add Beneficiary page
    When user enters account number "123456789012" and IFSC "QRST0001234"
    And clicks "Add Beneficiary"
    Then a success message "Beneficiary added successfully" is displayed

  Scenario: Transfer funds within limit
    Given user has a registered beneficiary "John Doe"
    When user initiates a transfer of amount "5000"
    And enters OTP "123456"
    Then the transfer is completed and confirmation is shown

  Scenario: OTP verification fails after three attempts
    Given user initiates a transfer
    When user enters incorrect OTP "111111" three times
    Then the transaction is cancelled and error message is displayed

  Scenario Outline: Transfer with various amounts
    Given user selects beneficiary "<beneficiary>"
    When user transfers amount "<amount>"
    And enters OTP "<otp>"
    Then the transfer should be "<result>"

    Examples:
      | beneficiary | amount | otp    | result   |
      | John Doe    | 5000   | 123456 | success  |
      | Jane Smith  | 150000 | 654321 | failure  |