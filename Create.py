import random

__author__ = 'twi'

class Create:

    def __init__(self,writeToFile,file,solver):
        self.sudoku = ['123456789', '456789123', '789123456', '214365897', '365897214', '897214365', '531642978', '642978531', '978531642']
        self.writeToFile = writeToFile
        self.file = file
        self.solver = solver
        self.createOneRandomCompleteSudoku(solver)

    def sudokuExists(self,sudoku):
        for i in self.sudokus:
            if self.equals(i,sudoku):
                return True
        return False

    def equals(self,s1,s2):
        x = 0
        while x < 9:
            y = 0
            while y < 9:
                if s1[x][y] != s2[x][y]:
                    return False
                y += 1
            x += 1
        return True

    def createOneRandomCompleteSudoku(self):
        return

    def callCreateOneRandomComplete(self):
        self.createOneRandomComplete(["         ","         ","         ","         ","         ","         ","         ","         ","         "],["","","","","","","","",""],["","","","","","","","",""],["","","","","","","","",""],0,0)

    def createOneRandomComplete(self,sudoku,x,y,z,i,j):
        #print(sudoku)
        if i == 8 and j == 8 and sudoku[i][j] != ' ':
            print(sudoku)
            self.solutions.append(sudoku)
            return
        elif sudoku[i][j] == ' ':
            if i < 3:
                a = 0
            elif i < 6:
                a = 1
            else:
                a = 2
            if j < 3:
                a += 0
            elif j < 6:
                a += 3
            else:
                a += 6
            for n in range(1,10):
                nStr = "{0}".format(n)
                if nStr not in x[i] and nStr not in y[j] and nStr not in z[a]:
                    sudokuCp = sudoku[:]
                    xCp = x[:]
                    yCp = y[:]
                    zCp = z[:]
                    xCp[i] = "{0}{1}".format(xCp[i], n)
                    yCp[j] = "{0}{1}".format(yCp[j], n)
                    zCp[a] = "{0}{1}".format(zCp[a], n)
                    sudokuCp[i] = "{0}{1}{2}".format(sudokuCp[i][0:j],n,sudokuCp[i][j+1:])
                    ni = i
                    nj = j
                    if nj == 8:
                        nj = 0
                        ni += 1
                    else:
                        nj += 1
                    if i == 8 and j == 8:
                        print(sudokuCp)
                        self.solutions.append(sudokuCp)
                        return
                    self.solve(sudokuCp,xCp,yCp,zCp,ni,nj)
        else:
            sudokuCp = sudoku[:]
            xCp = x[:]
            yCp = y[:]
            zCp = z[:]
            ni = i
            nj = j
            if nj == 8:
                nj = 0
                ni += 1
            else:
                nj += 1
            self.solve(sudokuCp,xCp,yCp,zCp,ni,nj)

""" mathias' code:
<head>
<title>-</title>
</head>
<body>
  <div id="WT"></div>
<script>

var sudoku=[];
Array.prototype.rotate = (function() {
    var unshift = Array.prototype.unshift,
        splice = Array.prototype.splice;

    return function(count) {
        var len = this.length >>> 0,
            count = count >> 0;

        unshift.apply(this, splice.call(this, count % len, len));
        return this;
    };
})();


function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex ;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}


function generate(){


 var lut=shuffle([1,2,3,4,5,6,7,8,9]);
 var rows=shuffle([shuffle([0,1,2]),shuffle([3,4,5]),shuffle([6,7,8])]);
 sudoku=[];
 for(var j0=0;j0<3;j0++){
  for(var j1=0;j1<3;j1++){
   var row=rows[j0][j1];
   console.log(row);
   sudoku[row]=lut.slice(0).rotate(j0+j1*3);
  }
 }
 var out="";
 for(var i=0;i<9;i++)
  out+=sudoku[i].join(",")+"<br>";
 document.getElementById("WT").innerHTML=out;
}



window.onload=generate();
</script>


</body>
</html>

"""

# ok - methoden machen die halt solve-methoden sind wie menschen das machen würden
# damit das ganze dann nach schwierigkeit sortieren...
# also zeilen shiften und dann noch die kästchen zeilenweise und generell shiften und dann noch zahlen tauschen...? i guess das war was der mathias gesagt hat

# zeilen- und spalten-weise permutationen in 3-er blöcken ausprobieren!! von einem einfachen sudoku das schon besteht

