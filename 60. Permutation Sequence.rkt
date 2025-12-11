;; https://leetcode.com/problems/permutation-sequence/
;; Racket practice for CS class
;; Build answer from most significant digit, avoid exponential runtime

(define (get-permutation n k)
  (lint->string (gen-perm (build-list n add1) (sub1 k)))
  )


(define (lint->string lst)  ; [1,2,3] -> "123"
  (list->string (map (lambda (x) (integer->char (+ 48 x))) lst)))


(define (get-idx arr i)  ; get arr[i]
  (first (foldr (lambda (cur res) (rest res))
                arr
                (build-list i +))))


(define (suffix arr i)  ; get arr[i:]
  (foldr (lambda (cur res) (rest res))
                arr
                (build-list i +)))


(define (del-idx arr i)  ; returns arr with index i removed
  (append (reverse (suffix (reverse arr) (- (length arr) i))) (suffix arr (add1 i))))


(define (fact n)  ; factorial, produces 1 for anything < 0
  (cond [(<= n 1) 1]
        [else (* n (fact (sub1 n)))]))


(define (gen-perm cur k)  ; get the k-th permutation of the list `cur`
  (local [(define amt (fact (sub1 (length cur))))
          (define idx (quotient k amt))]
    (cond [(empty? cur) empty]
          [else (cons (get-idx cur idx) (gen-perm (del-idx cur idx) (- k (* idx amt))))])))
