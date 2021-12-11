--
-- Data base: payments-1001
--

DROP DATABASE IF EXISTS payments;
CREATE DATABASE IF NOT EXISTS payments;
USE payments;

-- --------------------------------------------------------

--
-- Table structure for transaction entity
--

CREATE TABLE IF NOT EXISTS transaction (
    merchant_id int(15),
    state_pol varchar(32),
    risk decimal(8,2),
    response_code_pol varchar(255),
    reference_sale varchar(255),
    reference_pol varchar(255),
    sign varchar(255),
    extra1 varchar(255),
    extra2 varchar(255),
    extra3 varchar(255),
    payment_method int(15),
    payment_method_type int(15),
    installments_number int(15),
    value decimal(8,2),
    tax decimal(8,2),
    additional_value float(15),
    transaction_date timestamp,
    currency varchar(5),
    email_buyer varchar(70),
    cus varchar(70),
    pse_bank varchar(255),
    test varchar(2),
    description varchar(255),
    billing_address varchar(255),
    shipping_address varchar(255),
    phone varchar(25),
    office_phone varchar(25),
    account_number_ach varchar(255),
    account_type_ach varchar(255),
    administrative_fee decimal(8,2),
    administrative_fee_base decimal(8,2),
    administrative_fee_tax decimal(8,2),
    airline_code varchar(5),
    attempts int(12),
    authorization_code varchar(15),
    travel_agency_authorization_code varchar(15),
    bank_id varchar(255),
    billing_city varchar(255),
    billing_country varchar(5),
    commision_pol decimal(8,2),
    commision_pol_currency varchar(5),
    customer_number int(15),
    paymentDate timestamp,
    error_code_bank varchar(255),
    error_message_bank varchar(255),
    exchange_rate decimal(8,2),
    ip varchar(255),
    nickname_buyer varchar(255),
    nickname_seller varchar(255),
    payment_method_id int(15),
    payment_request_state varchar(255),
    pseReference1 varchar(255),
    pseReference2 varchar(255),
    pseReference3 varchar(255),
    response_message_pol varchar(255),
    shipping_city varchar(255),
    shipping_country varchar(5),
    transaction_bank_id varchar(255),
    transaction_id varchar(255),
    payment_method_name varchar(255), 
    date timestamp,
    franchise varchar(15),
    bank_referenced_name varchar(255),
    operation_date timestamp,
    cc_holder varchar(255),
    antifraudMerchantId int(25),
    transaction_type varchar(255), 
    cc_number varchar(255),
    cardType varchar(15),
    account_id int(25),
    bank_referenced_code varchar(15),
    pseCycle varchar(5)
);