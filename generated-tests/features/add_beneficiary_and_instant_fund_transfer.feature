Feature: Add Beneficiary and Instant Fund Transfer
  As a registered banking user
  I want to manage beneficiaries and transfer funds instantly
  So that I can send money securely and quickly

  Background:
    Given the user is logged into the mobile banking app
    And the user is on the Dashboard screen

  Scenario: Successfully add a beneficiary with valid details
    When the user navigates to the Add Beneficiary screen
    And the user enters a valid account number "123456789012"
    And the user enters a valid IFSC code "ABCD0123456"
    And the user enters beneficiary name "John Doe"
    And the user taps the "Add Beneficiary" button
    Then the system shows a success message "Beneficiary added successfully"
    And the new beneficiary appears in the beneficiary list

  Scenario: Fail to add beneficiary with invalid account number
    When the user navigates to the Add Beneficiary screen
    And the user enters an invalid account number "12AB34CD56"
    And the user enters a valid IFSC code "ABCD0123456"
    And the user taps the "Add Beneficiary" button
    Then the system shows an error message "Invalid account number format"

  Scenario: OTP lockout after three failed attempts
    Given a transfer has been initiated to beneficiary "John Doe"
    When the user enters an incorrect OTP "111111" and taps "Verify OTP"
    And the user repeats the incorrect OTP entry two more times
    Then the system displays "Maximum OTP attempts exceeded. Transaction cancelled."
    And the transaction is aborted

  Scenario Outline: Add beneficiary with edge case account number lengths
    When the user navigates to the Add Beneficiary screen
    And the user enters an account number "<accountNumber>"
    And the user enters a valid IFSC code "ABCD0123456"
    And the user enters beneficiary name "Edge User"
    And the user taps the "Add Beneficiary" button
    Then the system shows a success message "Beneficiary added successfully"

    Examples:
      | accountNumber   |
      | 1234567890      |  # minimum 10 digits
      | 1234567890123456|  # maximum 16 digits