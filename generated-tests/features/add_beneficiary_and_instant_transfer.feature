Feature: Add Beneficiary and Instant Transfer
  As a registered banking user
  I want to manage beneficiaries and perform instant fund transfers
  So that I can move money securely and quickly

  Background:
    Given the user is logged into the mobile banking app
    And the user has a valid authentication token

  Scenario: Add beneficiary with valid details
    When the user navigates to the Add Beneficiary page
    And the user enters account number "123456789012"
    And the user enters IFSC code "MNOP0123456"
    And the user enters beneficiary name "John Doe"
    And the user clicks the "Add Beneficiary" button
    Then the beneficiary is added successfully
    And a success message is displayed

  Scenario: Instant transfer within limit succeeds
    Given the user has a registered beneficiary "John Doe"
    When the user initiates a transfer of amount "5000" to "John Doe"
    And the user provides a valid OTP "654321"
    Then the transfer is completed
    And a confirmation message is shown
    And the transaction appears in history

  Scenario: Transfer fails after three invalid OTP attempts
    Given the user has a pending transfer of amount "2000"
    When the user enters OTP "111111" and submits
    And the user enters OTP "222222" and submits
    And the user enters OTP "333333" and submits
    Then the transaction is cancelled
    And an error message indicating OTP failure is displayed

  Scenario Outline: Transfer at edge amount limits
    When the user transfers <amount> to a registered beneficiary
    And provides a valid OTP "987654"
    Then the transfer should be <outcome>

    Examples:
      | amount | outcome |
      | 100000 | successful |
      | 0      | rejected |
