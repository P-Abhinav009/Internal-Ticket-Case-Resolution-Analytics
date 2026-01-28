-- Calculate Ticket Aging Buckets
SELECT 
    CASE 
        WHEN DATEDIFF(day, Created_Date, GETDATE()) <= 2 THEN '0-2 Days'
        WHEN DATEDIFF(day, Created_Date, GETDATE()) <= 5 THEN '3-5 Days'
        ELSE 'Over 5 Days'
    END AS Aging_Bucket,
    COUNT(Ticket_ID) AS Total_Tickets
FROM Internal_Tickets
WHERE Status != 'Closed'
GROUP BY 
    CASE 
        WHEN DATEDIFF(day, Created_Date, GETDATE()) <= 2 THEN '0-2 Days'
        WHEN DATEDIFF(day, Created_Date, GETDATE()) <= 5 THEN '3-5 Days'
        ELSE 'Over 5 Days'
    END;