#include <iostream>
#include <filesystem>
using namespace std;

std::uintmax_t directorySize(const std::filesystem::path& directory)
{
    std::uintmax_t size{ 0 };
    for (const auto& entry : std::filesystem::recursive_directory_iterator(directory))
    {
        if (entry.is_regular_file() && !entry.is_symlink())
        {
            size += entry.file_size();
            //cout << entry << "\n";
        }
    }
    return size;
}

int main()
{
    cout << "folder sizz: " << directorySize("../../");
}
