;; https://leetcode.com/problems/reverse-integer/description/
;; List to number conversions practice

(define/contract (reverse x)
  (-> exact-integer? exact-integer?)
    (cond [(zero? x) 0]
          [(< x 0) (- (rev (- x)))]
          [else (rev x)])
  )

(define (rev x)
  (local [(define ans (list->num (num->list x)))]
     (cond [(> ans (sub1 (expt 2 31))) 0]
           [(< ans (- (expt 2 31))) 0]
           [else ans])))

(define (list->num arr)  ; [1,2,3] -> 123
  (foldl (lambda (cur res) (+ cur (* 10 res)))
         0
         arr))

(define (num->list x)  ; naturally reverses, 123 -> [3,2,1]
  (cond [(zero? x) empty]
        [else (cons (remainder x 10) (num->list (quotient x 10)))]))
