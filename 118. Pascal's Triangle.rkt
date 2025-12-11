;; https://leetcode.com/problems/pascals-triangle/

(define/contract (generate numRows)
  (-> exact-integer? (listof (listof exact-integer?)))
   (reverse (pascal numRows));
  )

(define (pascal n)
  (foldr (lambda (cur res) (cons (new-row (first res)) res))
         (list (list 1))
         (build-list (sub1 n) +)))

(define (new-row row)  ; make the next row after cur
  (append (list 1) (sum-adj row) (list 1)))

(define (sum-adj row)
  (cond [(empty? (rest row)) empty]
        [else (cons (+ (first row) (second row)) (sum-adj (rest row)))]))
