// for the sake of describing multiple arguments, we use a struct
struct args {
	(void *) function;
	(void *) inp;
};

int hp(struct args s); // true if halts, false if not
void hpp(struct args s) {
	if (hp(s)) {
		while(1);
	}
}

int main(void) {
	struct args s;
	s.function = hpp; // for some reason dereferencing/referencing function pointers does nothing, c moment
	s.inp = &s;
  if (hpp(s)) {
    printf("Hpp halts!\n");
  } else {
    printf("Hpp does not halt!\n");
  }
}
