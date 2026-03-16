Feature: Add Beneficiary and Instant Fund Transfer
  Background:
    Given the user is logged in
  Scenario: Verify adding a beneficiary with valid account number and IFSC
    When the user enters a valid 12‑digit account number, a valid IFSC code, and a beneficiary name
    And taps the 'Add Beneficiary' button
    Then the system shows a success message and the beneficiary appears in the list
  Scenario: Verify transferring money to a registered beneficiary within limits
    Given a beneficiary is already added
    When the user selects the beneficiary and enters an amount of ₹5,000
    And proceeds to OTP and enters a correct OTP
    Then the transfer is completed and a success message is displayed
  Scenario: Verify OTP verification succeeds and transaction completes
    When the user enters the correct OTP on the OTP entry screen
    And taps 'Verify OTP'
    Then the OTP is validated and the transaction is processed successfully
  Scenario Outline: Verify adding beneficiary with account number length variations
    When the user enters an account number <accountNumber> and a valid IFSC
    And taps 'Add Beneficiary'
    Then the system should add the beneficiary successfully
    Examples:
      | accountNumber        |
      | 1234567890          |
      | 1234567890123456   |