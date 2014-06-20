/*
Assuming the following basic  table structure
Documents (DocID, DocDate)
Keywords (KeyWordID, KeyWord)
DocumentKeywords (DocID,KeyWordID)

Write a query to return the following:
Part 1: Documents with a DocDate after 4/1/1995  
Part 2: Documents that contain the keyword "Blue"  
Part 3: Documents that contain the either the keyword "Blue" or "Yellow"
Part 4: Documents that contain the both the keywords "Blue" and "Yellow"
Part 5: Documents that contain the both the keywords "Blue" or "Yellow" but not both.
*/


-- Part 1
SELECT DocID
FROM Documents
WHERE DocDate > '4/1/1995';


-- Part 2
SELECT doc.DocID
FROM Documents doc, DocumentKeywords dockey, Keywords key
WHERE doc.DocID = dockey.DocId
AND dockey.KeyWordID = key.KeyWordID
AND key.KeyWord = 'Blue';


-- Part 3
SELECT doc.DocID
FROM Documents doc, DocumentKeywords dockey, Keywords key
WHERE doc.DocID = dockey.DocId
AND dockey.KeyWordID = key.KeyWordID
AND key.KeyWord IN ('Blue', 'Yellow');


-- Part 4
WITH pivot AS (
  SELECT doc.DocID AS id,
    MAX(CASE WHEN key.Keyword = 'Blue' THEN True ELSE NULL END) AS blue,
    MAX(CASE WHEN key.Keyword = 'Yellow' THEN True ELSE NULL END) AS yellow
  FROM Documents doc, DocumentKeywords dockey, Keywords key
  WHERE doc.DocID = dockey.DocId
  AND dockey.KeyWordID = key.KeyWordID
)
SELECT id
FROM pivot
WHERE blue = True
AND yellow = True;


-- Part 5
WITH pivot AS (
  SELECT doc.DocID AS id,
    MAX(CASE WHEN key.Keyword = 'Blue' THEN True ELSE NULL END) AS blue,
    MAX(CASE WHEN key.Keyword = 'Yellow' THEN True ELSE NULL END) AS yellow
  FROM Documents doc, DocumentKeywords dockey, Keywords key
  WHERE doc.DocID = dockey.DocId
  AND dockey.KeyWordID = key.KeyWordID
)
SELECT id
FROM pivot
WHERE (blue = True and yellow = False)
OR (blue = False and yellow = True);
