class cats{
	public static double[][] convert(String[]exams, int n, int i, double[][] ret){
		if(i == n){
			return ret;
		} 
		else {
			double[] check = new double[ret[i].length];
			int badVariableName = 0;

			for(int b = 0; b< ret[i].length; b++){
				badVariableName = exams[i].indexOf(';');
				check[b] = Double.parseDouble(exams[i].substring(0, badVariableName));
				exams[i] = exams[i].substring(badVariableName+1);
		  	}

			ret[i] = check;

			return convert(exams, n, i+1, ret);
			}
	}
	public static void main(String[] args) {
        String[] exams = {"1;2;3;4;", "5;6;7;8;", "9;10;11;12;"};
        double[][] examArray = new double[exams.length][4];
        examArray = convert(exams, exams.length, 0, examArray);
        for (int i=0;i<exams.length;i++){
        	for (int j=0;j<4;j++){
        		System.out.print(examArray[i][j]+"\t");

        }
        System.out.println();
	}
}
}