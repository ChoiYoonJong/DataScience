select saname as "이름", sapay*10000 as "연봉", round(sapay*10000/12,-2) as "월급", trunc(sapay*10000/12*0.05,0) as "세금" from sawon;

