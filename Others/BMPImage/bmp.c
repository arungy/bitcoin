// BMP - Reader/Writer

#include <stdio.h>

//typedef
typedef unsigned char  BYTE;
typedef unsigned short WORD;
typedef unsigned int   DWORD;
typedef signed int     LONG;

//BMP - header
typedef struct tag_bmp_header {
    WORD   type;
    DWORD  size;
    WORD   reserved1;
    WORD   reserved2;
    DWORD  offset;

    DWORD  dib_header_size;
    LONG   width;
    LONG   height;
    WORD   num_planes;
    WORD   bits_per_pixel;
    DWORD  compression;
    DWORD  image_size_bytes;
    LONG   x_pixel_per_meter;
    LONG   y_pixel_per_meter;
    DWORD  num_colors;
    DWORD  important_colors;
} bmp_header_t;



int main(int argc, char *argv[])
{
    char *bmp_fname = "test.bmp";
    FILE *fp = NULL;

    bmp_header_t bmp_header;

    printf("\nBMP - Reader/Writer.");

    fp = fopen(bmp_fname, "r");
    if (NULL == fp) {
        printf("\nError: %s is not found.", bmp_fname);
        return 0;
    }

    DWORD sz = fread(&bmp_header, 1, sizeof(bmp_header_t), fp);
    if (sz != sizeof(bmp_header_t)) {
        printf("\n%s: header load error.", bmp_fname);
        return 0;
    }

    printf("\nBMP header type: %x",       bmp_header.type);
    printf("\nBMP header size: %d",       bmp_header.size);
    printf("\nBMP header offset: %d",     bmp_header.offset);
    printf("\nBMP dib_header_size: %d",   bmp_header.dib_header_size);
    printf("\nBMP width: %d",             bmp_header.width);
    printf("\nBMP height: %d",            bmp_header.height);
    printf("\nBMP num_planes: %d",        bmp_header.num_planes);
    printf("\nBMP bits_per_pixel: %d",    bmp_header.bits_per_pixel);
    printf("\nBMP compression: %d",       bmp_header.compression);
    printf("\nBMP image_size_bytes: %d",  bmp_header.image_size_bytes);
    printf("\nBMP x_pixel_per_meter: %d", bmp_header.x_pixel_per_meter);
    printf("\nBMP y_pixel_per_meter: %d", bmp_header.y_pixel_per_meter);
    printf("\nBMP num_colors: %d",        bmp_header.num_colors);
    printf("\nBMP important_colors: %d",  bmp_header.important_colors);

    if (fp) {
        fclose(fp);
        fp = 0;
    }

    return 1;
}