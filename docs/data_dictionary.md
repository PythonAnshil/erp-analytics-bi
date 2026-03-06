# ERP Data Dictionary

## customers
| column | type | description |
|------|------|-------------|
customer_id | serial | primary key |
customer_name | varchar | company name |
industry | varchar | industry sector |
city | varchar | customer location |
created_at | timestamp | record creation time |

## employees
| column | type | description |
employee_id | serial | primary key |
first_name | varchar | employee first name |
last_name | varchar | employee last name |
role | varchar | job role |
hourly_rate | numeric | billing rate |
hire_date | date | employment start |

## projects
| column | type | description |
project_id | serial | project identifier |
project_name | varchar | project title |
customer_id | int | client reference |
start_date | date | project start |
end_date | date | project end |
budget | numeric | project budget |
status | varchar | active/completed/on_hold |

## timesheets
| column | type | description |
timesheet_id | serial | entry id |
employee_id | int | employee reference |
project_id | int | project reference |
work_date | date | date worked |
hours_worked | numeric | hours logged |

## invoices
| column | type | description |
invoice_id | serial | invoice id |
project_id | int | project reference |
invoice_date | date | invoice issue |
due_date | date | payment deadline |
amount | numeric | invoice amount |
status | varchar | paid/pending/overdue |

## payments
| column | type | description |
payment_id | serial | payment id |
invoice_id | int | invoice reference |
payment_date | date | payment timestamp |
amount_paid | numeric | payment value |