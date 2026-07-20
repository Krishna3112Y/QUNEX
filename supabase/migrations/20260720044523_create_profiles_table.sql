-- Create the profiles table to store student identity and metrics
CREATE TABLE public.profiles (
    -- Field Name: id
    -- Data Type: UUID, Key Type: Primary Key, Rule: Must match auth.users
    id UUID REFERENCES auth.users(id) ON DELETE CASCADE PRIMARY KEY,

    -- Field Name: username
    -- Data Type: TEXT, Key Type: Unique Constraint, Rule: Cannot be duplicated
    username TEXT UNIQUE NOT NULL,

    -- Field Name: cash_balance
    -- Data Type: NUMERIC(15, 2), Default: 100000.00, Rule: CHECK cash_balance >= 0
    cash_balance NUMERIC(15, 2) DEFAULT 100000.00 NOT NULL CHECK (cash_balance >= 0),

    -- Field Name: created_at
    -- Data Type: TIMESTAMP, Default: NOW(), Rule: Records creation time automatically
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL
);
