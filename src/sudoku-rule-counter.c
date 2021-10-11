#include <stdio.h>
#include <stdbool.h>

#define WORLD_LENGTH (PROBLEM_SIZE*PROBLEM_SIZE)
#define WORLD_SIZE (WORLD_LENGTH*WORLD_LENGTH)

int valid_count = 0;
int max_depth   = 0;

typedef int world_t[WORLD_LENGTH][WORLD_LENGTH];

void print_world (world_t world)
{
  for (int line=0 ; line<WORLD_LENGTH ; line++) {
    for (int i=0 ; i<WORLD_LENGTH ; i++) printf("+-%s", (i==WORLD_LENGTH-1?"+\n":""));
    
    for (int i=0 ; i<WORLD_LENGTH ; i++) {    
      printf("|%c%s",
             (world[line][i]==0?' ':'0'+world[line][i]),
             (i==WORLD_LENGTH-1?"|\n":""));
    }
  }
  
  for (int i=0 ; i<WORLD_LENGTH ; i++) printf("+-%s", (i==WORLD_LENGTH-1?"+\n":""));
}

void init_world (world_t world)
{
  for (int y=0 ; y<WORLD_LENGTH ; y++) {
    for (int x=0 ; x<WORLD_LENGTH ; x++) {
      world[y][x] = 0;
    }
  }
}

static inline bool check_validity (world_t world, int y, int x, int value) {
  int y0 = (y/PROBLEM_SIZE)*PROBLEM_SIZE;
  int x0 = (x/PROBLEM_SIZE)*PROBLEM_SIZE;
  
  for (int i=0 ; i<WORLD_LENGTH ; i++) {
#ifdef ENABLE_ROW_RULE
      if (world[y][i]==value) return false;
#endif
#ifdef ENABLE_COLUMN_RULE
      if (world[i][x]==value) return false;
#endif
#ifdef ENABLE_BOX_RULE
      if (world[y0+i/PROBLEM_SIZE][x0+i%PROBLEM_SIZE]==value) return false;
#endif
#ifdef ENABLE_RISE_RULE
      if (world[(y+i)%WORLD_LENGTH][(x+i)%WORLD_LENGTH]==value) return false;
#endif
#ifdef ENABLE_FALL_RULE
      if (world[(WORLD_LENGTH+y-i)%WORLD_LENGTH][(x+i)%WORLD_LENGTH]==value) return false;
#endif
  }
  
  return true;
}

void cover_rec (world_t world, int index)
{
  if (index==WORLD_SIZE) {
    printf("New solution #%d:\n", valid_count++);
    print_world(world);
  } else {
#ifdef DEBUG_DEPTH 
    if (index>max_depth) {
      max_depth = index;
      printf("New maxdepth is %d\n", max_depth);
      print_world(world);
    }
#endif
    
    int y = index / WORLD_LENGTH;
    int x = index % WORLD_LENGTH;
    
    for (int value=1 ; value<=WORLD_LENGTH ; value++) {
      if (check_validity(world, y, x, value)) {
        world[y][x] = value;
        cover_rec(world, index+1);
        world[y][x] = 0;
      }
    }
  }
}

void cover_world (world_t world)
{
  // hardcode first line
  for (int x=0 ; x<WORLD_LENGTH ; x++) {
    world[0][x] = x+1;
  }
  
  cover_rec(world, WORLD_LENGTH);
}

int main (int argc, char* argv[])
{
  world_t world;
  
  init_world(world);
  cover_world(world);
  
  return 0;
}

