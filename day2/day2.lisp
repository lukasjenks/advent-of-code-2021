(ql:quickload "str")

(defun get-solution-one (puzzleInput)
  (let ((xVal 0)
		(yVal 0))
	(progn
	  (loop for moveAction in puzzleInput
		   do
		   (let ((direction (nth 0 (str:words moveAction)))
				 (units (parse-integer (nth 1 (str:words moveAction)))))
			 (cond
			   ((string-equal direction "forward") (incf xVal units))
			   ((string-equal direction "up")      (decf yVal units))
			   ((string-equal direction "down")	   (incf yVal units)))))
	  (* xVal yVal))))

(defun get-solution-two (puzzleInput)
  (let ((xVal 0)
		(yVal 0)
		(aim 0))
	(progn
	  (loop for moveAction in puzzleInput
		   do
		   (let ((direction (nth 0 (str:words moveAction)))
				 (units (parse-integer (nth 1 (str:words moveAction)))))
			 (cond
			   ((string-equal direction "forward") (progn (incf xVal units) (incf yVal (* aim units))))
			   ((string-equal direction "up")      (progn (decf aim units)))
			   ((string-equal direction "down")	   (progn (incf aim units))))))
	  (* xVal yVal))))

(defun load-puzzle-input (filename)
  (with-open-file (stream filename)
	(loop for line = (read-line stream nil)
		 while line
		 collect line)))

(defun main ()
  (let ((puzzle-input (load-puzzle-input "./day2puzzleinput.txt")))
	(print (get-solution-one puzzle-input))
	(print (get-solution-two puzzle-input))))

(main)
